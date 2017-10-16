'''
Created on Oct 11, 2017

@author: Administrator
'''
import urllib


class HtmlOutputer(object):
    
    def __init__(self):
        self.datas = []
    
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    
    def output_html(self):
        fout = open('output.html','w',encoding='utf-8')
        fout.write("<html>")
        fout.write("<meta charset=\"utf-8\" /> ")
        fout.write("<body>")
        fout.write("<table>")
        #ascii
        for data in self.datas:
            pp = str(data['summary'].encode('utf-8'),'utf-8')
            print('pp:'+pp)
            fout.write("<tr>")
            fout.write("<td>%s</td>" % str(data['url'].encode('utf-8'),'utf-8'))
            fout.write("<td>%s</td>" % str(data['title'].encode('utf-8'),'utf-8'))
            fout.write("<td>%s</td>" % pp)
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()
    
    
    
    



