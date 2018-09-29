# -*- coding: utf-8 -*-
from scrapy import Spider,Request
from zhihu_users.settings import *
from bs4 import BeautifulSoup
import json
import requests, redis,time
from zhihu_users.databaseOP import redisOP
from zhihu_users.items import ZhihuUsersItem
from zhihu_users.ip_proxies import ip_proxies
from zhihu_users.pageOP import pageOP

block_url = 'https://www.zhihu.com/account/unhuman?type=unhuman&message=%E7%B3%BB%E7%BB%9F%E6%A3%80%E6%B5%8B%E5%88%B0%E6%82%A8%E7%9A%84%E5%B8%90%E5%8F%B7%E6%88%96IP%E5%AD%98%E5%9C%A8%E5%BC%82%E5%B8%B8%E6%B5%81%E9%87%8F%EF%BC%8C%E8%AF%B7%E8%BF%9B%E8%A1%8C%E9%AA%8C%E8%AF%81%E7%94%A8%E4%BA%8E%E7%A1%AE%E8%AE%A4%E8%BF%99%E4%BA%9B%E8%AF%B7%E6%B1%82%E4%B8%8D%E6%98%AF%E8%87%AA%E5%8A%A8%E7%A8%8B%E5%BA%8F%E5%8F%91%E5%87%BA%E7%9A%84'

class StartVzchSpider(Spider):
    redisOP = redisOP.redisOP()
    ip_proxies = ip_proxies()
    pageOP = pageOP()
    name = 'start_vzch'
    allowed_domains = ['zhihu.com']
    # start_url = 'https://www.zhihu.com/people/excited-vczh/following'
    start_url = 'https://www.zhihu.com/people/zhong-sheng-8-46/following'
    def start_requests(self):
        item = self.redisOP.get_redis()
        url = 'https://www.zhihu.com/people/' + item[1] + '/following'
        yield Request(url,method='GET',headers=ZHIHU_HEADER, callback = self.parse, meta={'name':item[0], 'urlToken':item[1]})

    def parse(self, response):
        Nname = response.meta['name']
        NurlToken = response.meta['urlToken']
        print(response.meta)
        print("******************")
        base_url = response.url
        soup = BeautifulSoup(response.text,'lxml')
        # ====================following
        res = soup.find("div", id = "data")['data-state']
        res_json = json.loads(res)
        res_json['entities']
        users = res_json['entities']['users']
        following_list = dict()
        if len(users) == 1:
            print('no following')
        print('================ 1 ========================')
        for item in users:
            print(users[item]['name'])
            print(users[item]['urlToken'])
            following_list[users[item]['name']] = users[item]['urlToken']
        # ===================== total pages
        buttons = soup.find_all('button', class_ = "Button PaginationButton Button--plain")
        if len(buttons) == 0:
            print("just one page")
        else:
            print(buttons[-1].string)
            for number in range(2, int(buttons[-1].string)+1):
                nurl = base_url+ "?page=" + str(number)
                page_detail = self.get_page(nurl)
                users = self.analysis(page_detail, str(number), buttons[-1].string)
                if users == None:
                    pass
                else:
                    for item in users:
                        print(item[0])
                        print(item[1])
                        following_list[item[0]] = item[1]
        # ===========  followers   =============
        base_url = base_url[:-9]+ 'followers'
        followers_list = self.followers_parse(base_url)

        if Nname in following_list:
            following_list.pop(Nname)
        if Nname in followers_list:
            followers_list.pop(Nname)

        self.redisOP.store_redis(following_list)
        self.redisOP.store_redis(followers_list)
        print(following_list)
        print(followers_list)

        item = ZhihuUsersItem()
        item['username'] = Nname
        item['urltoken'] = NurlToken
        item['following'] = str(following_list)
        item['followers'] = str(followers_list)
        yield item

        self.redisOP.change_redis(Nname,NurlToken)
        items = self.redisOP.get_redis()
        if items == None:
            pass
        else:
            name = items[0]
            urlToken = items[1]
            next_url = 'https://www.zhihu.com/people/' + items[1] + '/following'
            print(next_url)
            yield Request(url = next_url, method='GET',headers=ZHIHU_HEADER, callback = self.parse, errback=self.errorprint, meta ={"name":name, 'urlToken':urlToken})

    def errorprint(self,failure):
        print(failure)
        print("redirect!")
        input()
        return

    def followers_parse(self, base_url):
        response = requests.get(url=base_url,headers = ZHIHU_HEADER)
        soup = BeautifulSoup(response.text,'lxml')
        # ====================followers
        res = soup.find("div", id = "data")['data-state']
        res_json = json.loads(res)
        res_json['entities']
        users = res_json['entities']['users']
        if len(users) == 1:
            print('no follower')
        followers_list = dict()
        print('================ 1 ========================')
        for item in users:
            print(users[item]['name'])
            print(users[item]['urlToken'])
            followers_list[users[item]['name']] = users[item]['urlToken']
        # ===================== total pages
        buttons = soup.find_all('button', class_ = "Button PaginationButton Button--plain")
        if len(buttons)<2:
            print("just one page")
        else:
            print(buttons[-1].string)
            for number in range(2, int(buttons[-1].string)+1):
                nurl = base_url+ "?page=" + str(number)
                print(nurl)
                page_detail = self.get_page(nurl)
                users = self.analysis(page_detail, str(number), buttons[-1].string)
                if users == None:
                    pass
                else:
                    for item in users:
                        print(item[0])
                        print(item[1])
                        followers_list[item[0]] = item[1]
        return followers_list

    def get_page(self, url):
        while True:
            flag = 3
            proxy = self.ip_proxies.get_proxy()
            print(proxy)
            # if proxy == None:
            #     page = requests.get(url = url, headers = ZHIHU_HEADER)
            # else:
            #     page = requests.get(url, headers = ZHIHU_HEADER, proxies = proxy, timeout = 3)
            #
            # page_detail = page.text
            # print(page_detail)
            # return page_detail
            while flag>0:
                try:
                    page = requests.get(url, headers = ZHIHU_HEADER, proxies=proxy, allow_redirects=False)
                    #, proxies=proxy, timeout = 5, allow_redirects=False)
                    if page.status_code == 301:
                        print("ok, this page maybe redirect page!")
                        input()
                        return
                    page_detail = page.text
                    return page_detail

                except requests.exceptions.ConnectionError:
                    print("ConnectionError -- please wait 5 seconds")
                    time.sleep(5)
                    flag = flag - 1
                except requests.exceptions.ChunkedEncodingError:
                    print('ChunkedEncodingError -- please wait 5 seconds')
                    time.sleep(5)
                    flag = flag - 1
                except:
                    print('Unfortunitely -- An Unknow Error Happened, Please wait 5 seconds')
                    time.sleep(5)
                    flag = flag - 1

    def analysis(self, page, flag, total):
        print('=========== ' +flag + ' ============ '+ total + ' ==============')
        soup = BeautifulSoup(page,'lxml')
        return_list = list()
        try:
            res = soup.find("div", id = "data")['data-state']
            res_json = json.loads(res)
            res_json['entities']
            users = res_json['entities']['users']
            for m in users:
                temp = list()
                temp.append(users[m]['name'])
                temp.append(users[m]['urlToken'])
                return_list.append(temp)
            if len(return_list) == 0:
                print("this page contain 0 message, maybe it is a block page!")
                input()
                return None
            return return_list
        except:
            print("analyze fail!")
            input()
            return None
