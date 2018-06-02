# 文本进度条V1

import time

scale = 100
print("执行开始".center(scale, '-'))

start = time.perf_counter()
for i in range(scale + 1):
    a = '>' * i
    b = '=' * (scale - i)
    c = (i / scale) * 100
    dur = time.perf_counter() - start
    print("{:^3.1f}%[{}{}]{:.2f}s".format(c, a, b, dur), end = "\r")
    time.sleep(0.02)

print("\n" + "执行结束".center(scale, '-'))