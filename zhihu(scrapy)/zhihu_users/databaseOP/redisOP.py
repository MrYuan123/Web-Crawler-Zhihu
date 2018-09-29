# -*- coding: utf-8 -*-
import redis

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

        keys = r.hkeys('ready')
        if len(keys) == 0:
            return None
        else:
            name = keys[0]
            urlToken = r.hget('ready',name)
            return [name,urlToken]

    def change_redis(self, name, urlToken):
        r = redis.Redis(host = '58.87.88.74', password = 'redispassword!', port = 6379, decode_responses=True)

        r.hdel('ready',name)
        r.hset('finish',name, urlToken)

        return 1
