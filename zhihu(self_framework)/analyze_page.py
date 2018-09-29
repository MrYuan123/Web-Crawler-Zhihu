# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import json

class analyze_page(object):
    def __init__(self):
        pass

    def first_analysis(self, page):
        soup = BeautifulSoup(page,'lxml')
        first_dict = dict()
        try:
            res = soup.find("div", id = "data")['data-state']
            res_json = json.loads(res)
            res_json['entities']
            users = res_json['entities']['users']
            for m in users:
                first_dict[users[m]['name']] = users[m]['urlToken']

            buttons = soup.find_all('button', class_ = "Button PaginationButton Button--plain")
            if len(buttons) == 0:
                print("just one page")
                totalPages = 1
            else:
                totalPages = int(buttons[-1].string)

            return_list = list()
            return_list.append(first_dict)
            return_list.append(totalPages)
            return return_list
        except:
            print("first page analyze failed!")
            input()
            return None


            # return [first_list, totalPages]

    def page_analysis(self, page):
        soup = BeautifulSoup(page,'lxml')
        return_dict = dict()
        try:
            res = soup.find("div", id = "data")['data-state']
            res_json = json.loads(res)
            res_json['entities']
            users = res_json['entities']['users']
            for m in users:
                return_dict[users[m]['name']] = users[m]['urlToken']
            return return_dict
        except:
            print("page analyze failed!")
            input()
            return None
            # return dict
