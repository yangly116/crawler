'''
Created on Oct 11, 2017

@author: Administrator
'''
import re

from bs4 import BeautifulSoup
import urllib.parse

class HtmlParser(object):
    
    
    def get_new_url(self, page_url, soup):
        new_urls = set()
        # /view/123.html
        links = soup.find_all('a',href=re.compile(r"/item/.*"))
        for link in links:
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls
    
    def get_new_data(self, page_url, soup):
        res_data = {}
        res_data['url'] = page_url
        #<dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        titil_note = soup.find('dd',class_ = 'lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = titil_note.get_text()
        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_note = soup.find('div',class_ = "lemma-summary")
        res_data['summary'] = summary_note.get_text()
        return res_data
        
    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return
        #print(html_cont)
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_url = self.get_new_url(page_url,soup)
        new_data = self.get_new_data(page_url,soup)
        return new_url,new_data
    



