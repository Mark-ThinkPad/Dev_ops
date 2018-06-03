# 你老婆的照片真好看
import requests
from bs4 import BeautifulSoup
import bs4
import os
     
def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
     
def fillUnivList(html):
    ulist = []
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup(class_='floor'):
        comment = str(tr.td).replace(str(tr.blockquote), '').replace(str(tr.small), '')
        ulist.append([comment])
    return ulist
     
def printUnivList(ulist):
    file = open("D://Github//Dev_ops//Task-试用期第4周//commits.txt", 'w+')
    file.write('\n'.join('%s' % id for id in ulist))
    file.close()
    print("文件保存成功")
         
def main():
    url = "https://bbs.hupu.com/20415703.html"
    html = getHTMLText(url)
    ulist = fillUnivList(html)
    printUnivList(ulist)

main()