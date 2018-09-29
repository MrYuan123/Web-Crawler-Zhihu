# -*- coding: utf-8 -*-
import analyze_page, databaseOP, get_page, redisOP

class start_crawl(object):
    def __init__(self):
        self.analyzePage = analyze_page.analyze_page()
        self.databaseOP = databaseOP.databaseOP()
        self.getPage = get_page.get_page()
        self.redisOP = redisOP.redisOP()

    def start_crawl(self):
        while True:
            # Get redis section
            try:
                next_item = self.redisOP.get_redis()
                username = next_item[0]
                urltoken = next_item[1]
                following_url = "https://www.zhihu.com/people/" + next_item[1] + '/following'
                followers_url = "https://www.zhihu.com/people/" + next_item[1] + '/followers'
                print(username)
                print(urltoken)
            except:
                print("get redis fail!")
                input()
                return

            # crawl list section
            followers_list = self.crawl_pages(username, followers_url, "followers")
            print("followes success!")
            following_list = self.crawl_pages(username, following_url, "following")
            print("following success!")


            if username in following_list:
                following_list.pop(username)
            if username in followers_list:
                followers_list.pop(username)

            # store database section
            item = dict()
            item["username"] = username
            item["urltoken"] = urltoken
            item["followers"] = str(followers_list)
            item["following"] = str(following_list)
            self.databaseOP.process_item(item)

            # store redis section
            self.redisOP.store_redis(following_list)
            self.redisOP.store_redis(followers_list)

            # change redis section
            self.redisOP.change_redis(username,urltoken)

        return

    def crawl_pages(self, name, baseurl, type):
        page_text = self.getPage.get_page(baseurl)
        first = self.analyzePage.first_analysis(page_text)
        totalPages = first[1]
        following_list = first[0]

        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("name:%s   page:1   total:%d   type:%s"%(name, totalPages,type))
        print(baseurl)
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(following_list)

        if totalPages == 1:
            return following_list
        else:
            for num in range(2, totalPages + 1):
                url = baseurl + "?page=" + str(num)
                page_text = self.getPage.get_page(url)
                temp_dict = self.analyzePage.page_analysis(page_text)

                print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("name:%s   page:%d   total:%d   type:%s"%(name, num, totalPages, type))
                print(url)
                print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print(temp_dict)

                for item in temp_dict:
                    following_list[item] = temp_dict[item]
            return following_list





if __name__ == "__main__":
    startCrawl = start_crawl()
    startCrawl.start_crawl()
