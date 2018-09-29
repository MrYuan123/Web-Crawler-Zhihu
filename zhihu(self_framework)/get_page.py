# -*- coding: utf-8 -*-
import requests,time
import redisOP, cookies, random

ZHIHU_HEADER = {
  # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
  # 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
  'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36',
  # 'cookie':'_zap=b7aad872-1ea1-4234-9072-04b703ad4bf5; __utmz=155987696.1526277864.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); q_c1=710d870d214c4159a8ba39855cc7917d|1527041393000|1524396091000; l_cap_id="OTFlMWZjYzFlOGY3NGU1ODkxN2MyNzViNmE1OWUwZjE=|1527056214|aaf344ccabcadec15be3ba3c299076389fe1c890"; r_cap_id="YTY0MTU3ZmM2N2ZiNDNkNDg0NjNmNzI5YTAyZThkYmU=|1527056214|c640fff69e24587329644d68246f41809a6f352b"; cap_id="NGRkOTVjNGE1NDNhNDU3ZTk0M2UxODM1OTkyOTAyNDc=|1527056214|9955bc92ca0c0f3c453dee3c66f2cf67c525c7ba"; __utma=155987696.1671948434.1526277864.1526980409.1527063259.7; d_c0="ADCmkZv4tA2PTpCEmktCJEXss0YZYOkz8JU=|1528263065"; _xsrf=0ac426c0-f553-45fc-aaef-0bb681f5882e; tgw_l7_route=8605c5a961285724a313ad9c1bbbc186; anc_cap_id=dd33800300884b7a84a5248eece091fe; capsion_ticket="2|1:0|10:1528699560|14:capsion_ticket|44:YWRjNzZhZGY1MDQ2NGNkOGIyNGIwNmJlZTc1YTJhNDY=|ba9d51d3651d1e813d978b8a104d824d6f6e5409596aab42a1e60f982d0ca5dd"',
}

class get_page(object):
    def __init__(self):
        self.redisOP = redisOP.redisOP()

    def get_page(self, url):
        now_header = ZHIHU_HEADER
        now_header['cookie'] = random.sample(cookies.cookies,1)[0]
        while True:
            flag = 3
            # proxy = self.redisOP.get_proxy()
            while flag>0:
                try:
                    page = requests.get(url, headers = now_header)
                    # print(page.headers) # , proxies=proxy, allow_redirects=False)
                    #, proxies=proxy, timeout = 5, allow_redirects=False
                    if page.url != url:
                        print("redirect!")
                        print(page.url)
                        input()
                    else:
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
