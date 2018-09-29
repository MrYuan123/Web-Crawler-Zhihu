# -*- coding: utf-8 -*-
import csv,requests
import random,time
from zhihu_users.ip_proxies import ip_proxies

class pageOP(object):
    def __init__(self):
        self.ip_proxies = ip_proxies()
        self.headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}

    def get_page(self, url):
        while True:
            flag = 3
            proxy = self.ip_proxies.get_ip()
            print(proxy)
            if proxy == None:
                page = requests.get(url = url, headers = ZHIHU_HEADER)
            else:
                page = requests.get(url = url, headers = ZHIHU_HEADER, proxies=proxies, timeout = 3)

            page_detail = page.text
            print(page_detail)
            return page_detail

            # while flag>0:
            #     try:
            #         if proxy == None:
            #             page = requests.get(url, headers = ZHIHU_HEADER)
            #         else:
            #             page = requests.get(url, headers = self.headers, proxies=proxies, timeout = 3)
            #
            #         page_detail = page.text
            #         return page_detail
            #     except requests.exceptions.ConnectionError:
            #         print("ConnectionError -- please wait 5 seconds")
            #         time.sleep(5)
            #         flag = flag - 1
            #     except requests.exceptions.ChunkedEncodingError:
            #         print('ChunkedEncodingError -- please wait 5 seconds')
            #         time.sleep(5)
            #         flag = flag - 1
            #     except:
            #         print('Unfortunitely -- An Unknow Error Happened, Please wait 5 seconds')
            #         time.sleep(5)
            #         flag = flag - 1

    def analysis(self, page, flag, total):
        print('=========== ' +flag + ' ============ '+ total + ' ==============')
        soup = BeautifulSoup(page,'lxml')
        res = soup.find("div", id = "data")['data-state']
        res_json = json.loads(res)
        res_json['entities']
        users = res_json['entities']['users']
        return_list = list()
        for m in users:
            temp = list()
            temp.append(users[m]['name'])
            temp.append(users[m]['urlToken'])
            return_list.append(temp)

        return return_list
