'''
Created on Oct 11, 2017

@author: Administrator
'''
import urllib


class HtmlDownloader(object):  
    
    def download(self,url):
        if url is None:
            return None
        respons = urllib.request.urlopen(url)
        if respons.getcode() != 200 :
            print('请求的url响应失败:'+url)
            return None
        return respons.read()
    



