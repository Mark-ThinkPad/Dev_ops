# 试用期第4周

`Time goes by` `时光荏苒`

---

### Part 1 : 本周所做

- 准备工作([视频教程](https://www.icourse163.org/learn/BIT-1001870001?tid=1002781006#/learn/content))

- 经过了一段时间的学习

![学习过程](https://github.com/Mark-ThinkPad/Dev_ops/blob/master/Task-%E8%AF%95%E7%94%A8%E6%9C%9F%E7%AC%AC4%E5%91%A8/screenshot/0.png)

- 爬虫的代码(<font color="dc143c">我先老实交代了有看过别人的代码，但是读懂也是花了一些时间，总是发现有很多视频教程里没讲到的东西，然后又去一个一个查......</font>)

这个四函数结构来自于[training/protraining/中国大学排名定向爬虫.py](https://github.com/Mark-ThinkPad/Dev_ops/blob/master/Task-%E8%AF%95%E7%94%A8%E6%9C%9F%E7%AC%AC4%E5%91%A8/training/protraining/%E4%B8%AD%E5%9B%BD%E5%A4%A7%E5%AD%A6%E6%8E%92%E5%90%8D%E5%AE%9A%E5%90%91%E7%88%AC%E8%99%AB.py)

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

![心情复杂](https://github.com/Mark-ThinkPad/Dev_ops/blob/master/Task-%E8%AF%95%E7%94%A8%E6%9C%9F%E7%AC%AC4%E5%91%A8/screenshot/1.png)

---

### Part 2 : 遇到的问题

- debug, debug, debug...最终以正常运行的状态提交上去(Python的debug有一种说不出来的感jio)

---

### Part 3 : 本周感想

- 为什么会这样呢？去年第一次接触了Linux发行版，前段时间又匆匆学习了html,js,python的基本语法。这两件快乐的事情叠加在一起，而这两份快乐，带给我的是更多的快乐。得到的，本应该是像梦境一般的时间...但是，为什么，我会变成这样的辣鸡萌新呢.....(打死白学家)

---

### Part 4 : 下周计划

- 更新一版全自主编写的爬虫

---

### Part 5 : 相对学长学姐说的话

- 长大在线里面个个都是人才，说话又好听，我超喜欢在里面的
