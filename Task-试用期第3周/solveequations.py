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
