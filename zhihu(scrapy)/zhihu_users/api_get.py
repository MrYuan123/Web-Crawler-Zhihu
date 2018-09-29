# -*- coding: utf-8 -*-
import requests,csv,json
import time

def get_proxies():
    url = "http://dec.ip3366.net/api/?key=20180606095251809&getnum=100&anonymoustype=4&formats=2&proxytype=0"
    results = requests.get(url)
    resultdetail = results.text
    print(resultdetail)
    jsonlist = json.loads(resultdetail)

    with open("ip_pool.csv",'w') as f:
        writer = csv.writer(f)
        for item in jsonlist:
            htmln = "http://" + str(item["Ip"]) + ":" + str(item["Port"])
            print(htmln)
            writer.writerow([htmln])

if __name__ == "__main__":
    while True:
        get_proxies()
        print('sleep 60s')
        time.sleep(60)
