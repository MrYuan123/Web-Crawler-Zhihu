# -*- coding: utf-8 -*-
import csv,requests
import random

class ip_proxies(object):
    def __init__(self):
        pass
    #     self.ipPOOL = self.build_pool()
    #     self.headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
    #
    # def build_pool(self):
    #     csvfile = open('zhihu_users/proxiesPOOL.csv','r')
    #     # csvfile = open('proxiesPOOL.csv','r')
    #     reader = csv.reader(csvfile)
    #     temp = list()
    #     for item in reader:
    #         temp.append(item[0])
    #     return temp
    #
    #
    # def get_ip(self):
    #     badNum = 0
    #     goodNum = 0
    #
    #     while True:
    #         proxy = random.sample(self.ipPOOL,1)
    #         print(proxy)
    #         proxy_url = str(proxy[0])
    #         if proxy_url == 'local':
    #             return None
    #         else:
    #             proxies = {'http':proxy_url}
    #             flag = 3
    #             while flag>0:
    #                 try:
    #                     page = requests.get('https://www.zhihu.com/people/ren-zha-xiao-xi-feng/followers', headers = self.headers, proxies=proxies, timeout=3)
    #                     # print(page.text)
    #                     print('good proxy')
    #                     return proxies
    #                 except:
    #                     flag = flag - 1
    #                     print('bad proxy')
    #                     print(proxies)


    def get_proxy(self):
        with open('zhihu_users/ip_pool.csv') as f:
            reader = csv.reader(f)
            temp = list()
            for item in reader:
                temp.append(item[0])
            returnproxy = random.sample(temp,1)
            return {'http':returnproxy[0]}
        # for item in self.ipPOOL:
        #     # proxies = {'http':str(item[0]).replace(" ",'')}
        #     proxy_url = str(item[0])
        #     proxies = {'http':proxy_url}
        #
        #     try:
        #         print(proxies)
        #         page = requests.get('http://pmmp.cnki.net/cdd/Disease/dis_detail.aspx?id=37140&SearchType=2', headers = self.headers, proxies=proxies, timeout=3)
        #         page_datail = page.text
        #         goodNum +=1
        #         with open("proxiesPOOL.csv", 'a' ,newline='') as f:
        #             writer = csv.writer(f)
        #             writer.writerow([proxy_url])
        #         print('good proxy')
        #     except:
        #         badNum+=1
        #         print('bad')



            # try:
            #     page = requests.get('http://pmmp.cnki.net/cdd/Disease/Dis_Catalog.aspx', headers = self.headers, proxies=proxies, timeout=3)
            #     page_detail = page.text
            #     with open("good_ips.csv", 'a' ,newline='') as f:
            #         writer = csv.writer(f)
            #         writer.writerow([str(item[0]).replace(" ",'')])
            #
            #     print('good proxy')
            #     goodNum +=1
            # except requests.exceptions.ConnectionError:
            #     print("ConnectionError")
            #     badNum +=1
            # except requests.exceptions.ChunkedEncodingError:
            #     print('ChunkedEncodingError')
            #     badNum +=1
            # except:
            #     badNum +=1
            #     print('Unfortunitely')



# if __name__ == '__main__':
#     f = ip_proxies()
#     proxy = f.get_ip()
#     print(proxy)
