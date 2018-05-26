# 试用期第三周

`working` `图片刷新速度看github服务器的脸色` `ps1是powershell的脚本文件`

---

### Part 1 : 本周所作

- 关于前言的准备

[JS非视频教程](https://www.imooc.com/learn/36), [Python视频教程](https://www.icourse163.org/learn/BIT-268001?tid=1002788003#/learn/announce), [菜鸟教程](https://www.runoob.com/)

- 关于JS基础入门

直接上图(源码在[试用期第1周的文件夹里](https://github.com/Mark-ThinkPad/Dev_ops/tree/master/Task-%E8%AF%95%E7%94%A8%E6%9C%9F%E7%AC%AC1%E5%91%A8))

![1](https://github.com/Mark-ThinkPad/Dev_ops/blob/master/Task-%E8%AF%95%E7%94%A8%E6%9C%9F%E7%AC%AC3%E5%91%A8/screenshot/1.png)

![2](https://github.com/Mark-ThinkPad/Dev_ops/blob/master/Task-%E8%AF%95%E7%94%A8%E6%9C%9F%E7%AC%AC3%E5%91%A8/screenshot/2.png)

![3](https://github.com/Mark-ThinkPad/Dev_ops/blob/master/Task-%E8%AF%95%E7%94%A8%E6%9C%9F%E7%AC%AC3%E5%91%A8/screenshot/3.png)

- 关于Python入门

1. Python开发环境的搭建（[教程](https://blog.csdn.net/u010159842/article/details/55260204)）

2. 解一元二次方程(Python3.5.2)([源文件](https://github.com/Mark-ThinkPad/Dev_ops/blob/master/Task-%E8%AF%95%E7%94%A8%E6%9C%9F%E7%AC%AC3%E5%91%A8/solveequations.py))

```python
#solve equations 解方程(translated by YouDaoDict)

#引入开方函数
from math import sqrt

#(I)输入数据, 我们默认使用该程序的人了解一元二次方程的求根公式以及韦达定理
print("假定方程为ax^2+bx+c=0")
a = float(input("请输入方程中的a: "))
b = float(input("请输入方程中的b: "))
c = float(input("请输入方程中的c: "))

#(P)处理数据, (O)输出结果
delta = b * b - 4 * a * c  #delta就是求根公式里的那个delta

#对delta三种情况进行分类处理
if a == 0 and b == 0:
    print("你是真的皮，再运行一次正常输入吧")
elif delta == 0:
    print("方程有且只有一个实数根,x = %.2f"%(-b / a / 2))
elif delta < 0:
    print("方程无实数解")
elif delta > 0:
    print("方程有两个解，x1 = %.2f, x2 = %.2f"%((-b + sqrt(delta)) / (2 * a),(-b - sqrt(delta)) / (2 * a)))
```

3. 安装beautifulsoup4的第三方库

- 偷偷在windows平台搞了一下

![4](https://github.com/Mark-ThinkPad/Dev_ops/blob/master/Task-%E8%AF%95%E7%94%A8%E6%9C%9F%E7%AC%AC3%E5%91%A8/screenshot/4.png)

- 然后进Linux mint里面再操作一下

![5](https://github.com/Mark-ThinkPad/Dev_ops/blob/master/Task-%E8%AF%95%E7%94%A8%E6%9C%9F%E7%AC%AC3%E5%91%A8/screenshot/5.png)

---

### Part 2 : 遇到的问题（全部已经解决）

- Linux mint上有py2.7和py3.5，但是系统桌面环境需要用到py2.7，然而我选择用py3.5(不兼容上一个大版本)，那么配置开发环境和安装bs4第三方库的时候出现了多次忘记加3这个数字导致的尴尬场面（Ubuntu18.04已经不自带py2了)(manjora的安装包我已经准备好了，不玩桌面环境准备入坑窗口管理器了，计划在暑假有时间了再搞，现在学业为重)

- 我记不起来了，搞py前面肯定有几次小问题的

---

### Part 3 : 本周感想

- 我还是比较适合视频教程，干巴巴的一堆文字和一个在线代码编辑框有些令我不适...于是我选了中国大学mooc上的python视频教程，效果还是不错的

- python的有些内容和c语言比较近似，所以很容易去理解

---

### Part 4 ： 下周计划

- 不小心看到task-4了，爬虫走起

---

### Part 5 ： 相对学长学姐说的话

- 有什么Linux发行版可以推荐的吗？debian系和非debian系都可以(deepin这个养老用的系统就算了，ubuntu免谈,linux mint正在用，我也不想kali学的好，局子进的早)
