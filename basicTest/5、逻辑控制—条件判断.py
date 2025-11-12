'''
条件判断： if

条件语法：

if 条件:
    条件为真的操作
    条件为真的操作
else:
    条件为假的操作
    条件为假的操作
    条件为假的操作
'''

if 3 > 5:
    print("AAAAAAA")
    print("BBBBBBB")

print("------------------------------------------->")

if 10 > 5:
    print("AAAAAAAAAAAA")
else:
    print("BBBBBBBBBBBBB")

print("------------------------------------------->")

# if ..... elif ..... elif ........ else .........

score = int(input("分数: "))

if score > 90 and score <= 100:
    print("优秀")
elif score > 80 and score <= 90:
    print("良好")
elif score > 70 and score <= 80:
    print("中等")
elif score > 60 and score <= 70:
    print("及格")
elif score > 0 and score <= 60:
    print("不及格")
else:
    print("输入的分数有误")
