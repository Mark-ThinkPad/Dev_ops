# 试用期第4周

`Time goes by` `时光荏苒`

---

### Part 1 : 本周所做

- 准备工作([视频教程](https://www.icourse163.org/learn/BIT-1001870001?tid=1002781006#/learn/content))

- 经过了一段时间的学习

![学习过程](https://github.com/Mark-ThinkPad/Dev_ops/blob/master/Task-%E8%AF%95%E7%94%A8%E6%9C%9F%E7%AC%AC4%E5%91%A8/screenshot/0.png)

- 爬虫的代码(<font color="dc143c">我先老实交代了有看过别人的代码，但是读懂也是花了一些时间，总是发现有很多视频教程里没讲到的东西，然后又去一个一个查......</font>)

```python
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
```

- 爬到的评论直接放在txt文件里了没做处理

!()[]

