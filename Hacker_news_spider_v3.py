# -*- coding: utf-8 -*-
"""
Created on Wed Sep 06 17:47:11 2017

@author: gh

翻页版本。查询范围：最新210条

python版本：2.7
"""

from bs4 import BeautifulSoup   #导入bs4库
import urllib2   # 网络访问模块

'''
#设置代理
#防止经常刷新页面造成页面访问被拒绝

enable_proxy = True
proxy_handler = urllib2.ProxyHandler({"http" : 'http://some-proxy.com:8080'})
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)
'''

file=open('After_Keyword_extraction.txt','w') #存储关键字提取后题目和网址的txt文档
HNpages = ["",
           "?next=15189690&n=31",
           "?next=15189398&n=61",
           "?next=15189228&n=91",
           "?next=15188996&n=121",
           "?next=15188683&n=151",
           "?next=15188426&n=181"]    #Hacker News网站前8页的部分网址
PageReqCounter = 1    #标记当前响应的页面页码
for page in HNpages:
    request = urllib2.Request("https://news.ycombinator.com/newest"+str(page))
    try:
        response = urllib2.urlopen(request)    #回传接收到的网页信息
    except urllib2.HTTPError, e:
        print e.code
    except urllib2.URLError, e:
        print e.reason
    else:
        print "Successfully request on page " + str(PageReqCounter)
        
    soup = BeautifulSoup(response.read())
    #print soup.prettify()    #格式化输出网页所有信息
    tags = soup.find_all('a',class_='storylink',rel='nofollow')              
    news_list = []       
    for tag in tags:
        news_dict = {}
        news_dict['News_title'] = tag.string
        news_dict['News_url'] = tag.get('href')
        news_list.append(news_dict)
    
    for i in news_list:  
        if 'deep learning' in i.get('News_title') or 'Deep Learning' in i.get('News_title'):
            file.write(str((i.get('News_title')).encode('utf-8')))
            file.write('\n')
            file.write(str((i.get('News_url')).encode('utf-8')))
            file.write('\n\n') 
    print "Page" + str(PageReqCounter) +" finish searching."   
    PageReqCounter = PageReqCounter + 1         
#end of for
file.close()
 
