# -*- coding: utf-8 -*-
import redis
from random import choice

class redisOP(object):
    def __init__(self):
        pass

    def store_redis(self, userlist):
        r = redis.Redis(host = '58.87.88.74', password = 'redispassword!', port = 6379, decode_responses=True)

        for item in userlist:
            if r.hexists('finish',item):
                print("finish!")
            else:
                if r.hexists('ready',item):
                    print("existed!")
                else:
                    r.hset('ready', item, userlist[item])
                    print("add!")

        return 1

    def get_redis(self):
        r = redis.Redis(host = '58.87.88.74', password = 'redispassword!', port = 6379, decode_responses=True)

        return_data = r.hscan('ready')
        return_dict = return_data[1]
        if len(return_dict) == 0:
            return None
        else:
            return_keys = list(return_dict.keys())
            name = choice(return_keys)
            return [name,return_dict[name]]

    def change_redis(self, name, urlToken):
        r = redis.Redis(host = '58.87.88.74', password = 'redispassword!', port = 6379, decode_responses=True)

        r.hdel('ready',name)
        r.hset('finish',name, urlToken)

        return 1
