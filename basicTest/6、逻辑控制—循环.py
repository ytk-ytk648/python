'''
循环的语法结构： for, while
'''

'''
for 变量 in 取值列表:
    执行的操作
    执行的操作
    执行的操作

取值列表: 
    range(), 生成多个连续的数字
        range(10), 默认从0开始， 生成10个数   0 1 2 3 4 5 6 7 8 9 
        range(1, 11),                     1 2 3 4 5 6 7 8 9 10 
'''

# ssh root@10.1.1.1......10.1.1.5
for i in range(1, 6):
    print("ssh root@10.1.1.%s" % i)

print("------------------------------------------->")

# 中断循环  continue  中断本次循环
for i in range(1, 6):
    if i == 3:
        continue
    print("ssh root@10.1.1.%s" % i)

print("------------------------------------------->")

# 中断循环  break  中断所有循环
for i in range(1, 6):
    if i == 3:
        break
    print("ssh root@10.1.1.%s" % i)

print("------------------------------------------->")

'''
while循环语法：

while 条件:
    执行的操作
    执行的操作
    执行的操作
'''

sum = 0
i = 1

while i <= 100:
    sum += i
    i += 1

print("结果： ", sum)

print("------------------------------------------->")

'''
while True:
    执行的操作
    执行的操作
    执行的操作
'''

import time

while True:
    print("Python中的while True循环测试.........")
    time.sleep(0.5)
