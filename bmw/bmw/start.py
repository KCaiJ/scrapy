__author__ = 'root'
from scrapy import  cmdline
if __name__ == '__main__':
    cmdline.execute("scrapy crawl bmw5".split())
   # cmdline.execute("scrapy gensipder -c crawl [爬虫名字] [域名]".split())