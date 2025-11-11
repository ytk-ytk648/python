#
# 正则表达式模块 : re
# 正则表达式：元字符
#
# 一、匹配单个字符
#     [0-9]           \d  单个数字,    \D  不是单个数字
#     [a-zA-Z]        \w  单个字母,    \W  不是单个字母
#     [[:space:]]     \s  单个空白,    \S  不是单个空白
#
# 二、匹配次数
#     *， +， ？,  {3}   {3,}    {3,5}
#
# 三、匹配位置
#
#     ^, $


test_str = "杨帅 love 峰哥"

import re

# search()过滤数据，能过滤到数据返回匹配对象 match object， 无法过滤到数据返回None
is_match = re.search(r"l..e", test_str)

if is_match:
    print("可以匹配到数据")
    # 获取匹配对象中的数据, 匹配对象.group()
    print(is_match.group())
else:
    print("未找到")
