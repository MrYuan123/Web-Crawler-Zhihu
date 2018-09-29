# -*- coding: utf-8 -*-

# Scrapy settings for zhihu_users project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihu_users'

SPIDER_MODULES = ['zhihu_users.spiders']
NEWSPIDER_MODULE = 'zhihu_users.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhihu_users (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#      'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
# }

ZHIHU_HEADER = {
  # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
  # 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
  'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36',
  'cookie':'q_c1=710d870d214c4159a8ba39855cc7917d|1524396091000|1524396091000; _zap=b7aad872-1ea1-4234-9072-04b703ad4bf5; aliyungf_tc=AQAAABCnZDN+fQcAsin/cmND5NGl8AcN; _xsrf=8d01d7f1-f665-4f96-8d88-30653e07eb02; d_c0="AOBgcQ-afA2PTraAxIdGIXsOdo0vuDtUDrE=|1524480184"; l_n_c=1; n_c=1; capsion_ticket="2|1:0|10:1526261959|14:capsion_ticket|44:ZDRhYTgwNmFkMTNiNDQ4N2FhMjMwNjRjZjFjNzc3MjE=|a417fde8d6009f5707b8d9d78a75e9fb7cfa5c1cb1d0e403629ef73058950d3e"; l_cap_id="YmQ1YjZjZmRiYmQzNDBhMGExODdkNzcyYjkxM2U5NDQ=|1526266420|21e69a378b7861931ec18db5e5dbc5ad98300639"; r_cap_id="MmQxYmRkNTdmM2IxNDQ5NWI0YWRiOTcwMzc1NGI0MDY=|1526266420|63193471243b91882d6f7d4cdb9ab5273a9c6d33"; cap_id="OTA5MzhkNDdmMTJkNGJjNjlmY2M5OTA3NmNjMzA2ZTg=|1526266420|af20d6cfe8d28c66465e506be831220e42eb75cb"; __utma=155987696.1671948434.1526277864.1526277864.1526277864.1; __utmb=155987696.0.10.1526277864; __utmc=155987696; __utmz=155987696.1526277864.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhihu_users.middlewares.ZhihuUsersSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'zhihu_users.middlewares.ZhihuUsersDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'zhihu_users.pipelines.ZhihuUsersPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

MYSQL_HOST = '140.143.128.221'
MYSQL_PORT = 2115
MYSQL_USER = 'gpsroot'
MYSQL_DBNAME = 'gps_ai_doctor'
MYSQL_PASSWORD = 'Woyaofacluster8!'
