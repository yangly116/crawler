'''
Created on Oct 11, 2017

@author: Administrator
'''


class UrlManager(object):
    
    def __init__(self):
        self.new_urls = set()#未爬取的url
        self.old_urls = set()#已经爬取过url
    def add_new_url(self,url):#添加单个url
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            #self.add_new_urls(url)
            self.new_urls.add(url)

    def add_new_urls(self,urls):#添加批量url
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.add_new_url(url)
    
    def has_new_url(self):#是否有带爬取的url
        return len(self.new_urls) != 0

    def get_new_url(self):#获取一个带爬取的url
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    
    
    
    
    
    
    
    



