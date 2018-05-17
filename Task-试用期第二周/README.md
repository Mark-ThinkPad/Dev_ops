# 试用期第二周

`开工中`

---

### Part 1 : 本周所做

`有截图` 

1. 关于前言的准备

在慕课网上找到一个位置比较靠前的免费教程：[Tony的Linux教程0](https://www.imooc.com/learn/175), [Tony的Linux教程1](https://www.imooc.com/learn/111) (PS:不能像上个星期那样突击学习了，效果不好，把内容动态的分配到每天，这样效果好一些)

2. 关于任务说明 &　任务

- 首先证明我用的是虚拟机(其实我有一台学生特惠的阿里云的windows服务器，目前用来挂机器人了)

![虚拟机](http://static.zybuluo.com/Mark201802/qq5ngj31zh6tu49fvlsw60r4/image_1cde78nrn14301j461stp1jhf1utc19.png)

![虚拟机内登录](http://static.zybuluo.com/Mark201802/gtp48rpy3viskle5e77f6mff/image_1cde7et6co1i91i16j11pd2q4126.png)

- 再证明我是用远程连接工具连接的

<font color="dc143c">(截图的时候校园网又双叒叕出问题了......不是别的地方有问题......)</font>

![Final Shell](http://static.zybuluo.com/Mark201802/wi1yneytrfyqe1j86nq3mga8/image_1cde7siul1gbj1n1rfnvjkm81n33.png)

- 搭建Lamp

1. 先手动修改一下yum源

[参考教程0](http://mirrors.163.com/.help/centos.html), [参考教程1](https://www.ruooo.com/VPS/594.html)

![修改过程0](http://static.zybuluo.com/Mark201802/1ssrmojz5pa346vyiujy4tax/image_1cdea0ure174oe04l6d13bu17f540.png)

(出现了大写字母O和数字0不分的尴尬情况......)

![修改过程1](http://static.zybuluo.com/Mark201802/o9krwdpexldpq04nlsz0g8c3/image_1cdea68f01bc3n97ssg92kae4d.png)

![修改过程2](http://static.zybuluo.com/Mark201802/zf8b0qqdn8qj7ajivvsdua45/image_1cdea8gfumiq1cnc1i5g1kq6qdo4q.png)

2. [参考教程](https://blog.csdn.net/u011277123/article/details/77847360)

![P0](http://static.zybuluo.com/Mark201802/2rgitu53o40lxu2odzvopgco/image_1cdeacmh3ij0olh1ok311uuktl57.png)

![P1](http://static.zybuluo.com/Mark201802/x9ceebyx000gis6m2fl1h63v/image_1cdeaenhc1qec1b2gs9012p81mie6k.png)

![P2](http://static.zybuluo.com/Mark201802/bwlulktkcwblhggcdac7tyo2/image_1cdeag51c193t10b1qvq27mnl071.png)

![P3](http://static.zybuluo.com/Mark201802/2ptfpr6qwml42vw7vegod1yv/image_1cdealnv2fhsqm41ju5gg41tae8b.png)

3. 创建/var/www/ops并修改Apache服务器的根目录到这里

![创建](http://static.zybuluo.com/Mark201802/0yaebsqu23si1w0oz2n1iqqz/image_1cdes485qi9eiut6ooi9fkt59.png)

![修改根目录](http://static.zybuluo.com/Mark201802/8rge1mojjddlchw00ggd9cq6/image_1cdet7f801n8g1nnd6ol17iq1t4c1m.png)

4. 把自己上周写的网站放上去

![效果图](http://static.zybuluo.com/Mark201802/4tsum1b5pzbceunlh7bjhuvt/image_1cdfhr9vkghj17521auhqqj1vne9.png)

5. 参考教程：[修改根目录](https://www.osyunwei.com/archives/789.html), [搭建LAMP](http://www.jb51.net/os/188488.html), [修改服务器端口](https://zhidao.baidu.com/question/6966481.html), [安装MariaDB](https://jingyan.baidu.com/article/25648fc182a7a99191fd0096.html), [使用清华大学的源快速下载安装MariaDB](https://blog.csdn.net/zh237560547/article/details/74783513), [配置Lamp](https://blog.csdn.net/qq_20948497/article/details/78451783)

6. 部分效果图

![php](http://static.zybuluo.com/Mark201802/xnuo4b7t3xtej5349sh8rzyo/image_1cdgtgd9c18dpoats3k9511ogt9.png)

![apache](http://static.zybuluo.com/Mark201802/ifxrs05evopwae864hyk37lm/image_1cdgthrsvepb122l1omc19sm12q7m.png)

- 写(找)一个能够自动上传到github的脚本(为什么是找啊......因为我对脚本语言一无所知，所以还得找视频教程学学脚本语言,[教程0](https://space.bilibili.com/267262953/#/),[教程1](https://www.bilibili.com/video/av21816585?from=search&seid=1131567582177017051),[教程2](https://www.imooc.com/u/279399/courses?sort=publish))

[脚本参考教程](https://blog.csdn.net/alanzjl/article/details/50715870), [作者的github库](https://github.com/alanzjl/MyConsoleTools)

![给学长学姐看看效果图](http://static.zybuluo.com/Mark201802/s3qoru2ua25p32ilbbw5ec3b/image_1cdiab8ra1ff910lt3rl1hht9n49.png)

---

### Part 2 : 遇到的问题

- 未解决的问题:Apache更改端口为80后无法访问网站(在培训中在同学和学长的帮助下解决，发现是防火墙的问题)

问题已解决：在firewall里设置开启8080端口

![解决问题后](http://static.zybuluo.com/Mark201802/n85k4sozupen7m7tmzmzkk55/image_1cdmgcrjqqt2617a2vmbn1htp.png)

- 解决的问题:
1. vim的自动缩进不是标准的四个空格(改配置文件)
2. 桥接网络模式下虚拟机竟然不能软件的更新和下载(发现是校园网的问题，手机开热点解决之，反正流量多)
3. 网易的源无法下载安装MariaDB数据库(按照教程写了一个repo文件从清华大学的源下载)
4. 第一次在Apache里放入自己上次的网站之后无法访问(通过寻找在Part1里提到的教程解决之)

---

###  Part 3 : 本周感想

- 命令行真的挺有意思，不用鼠标点来点去了，但是目前还是需要习惯一下没有GUI的日子
- 还需要多多了解很多命令行操作(话说我买了一个Linux程序员水杯，杯子上专门印着Linux基本命令)
- 我用键盘打中文和打英文的速度严重不一致......以后多敲敲命令......
- 我永远喜欢Linux.jpg
- 我的Ubuntu 18.04 LTS又吃灰了一个星期

---

### Part 4 : 下周计划

从目前的知识盲区来看，有三点可以深入一下：1. Linux基本命令 2. shell编程 3. Python ，所以需要每天日积月累的一点一点学。


---

### Part 5 : 想对学长学姐说的话

- 