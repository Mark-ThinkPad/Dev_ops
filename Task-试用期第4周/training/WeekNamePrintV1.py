# WeekNamePrintV1.py

weekstr = "星期一星期二星期三星期四星期五星期六星期日"
weekId = eval(input("请输入关键字(1-7):"))
pos = (weekId - 1) * 3
print(weekstr[pos:pos+3])