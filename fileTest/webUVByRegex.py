# 用户访问量      客户端地址: x.x.x.x    访问次数: xxxxx
import re


def webUvByRegex(web_log):
    # 规划字典，统计次数  {"客户端地址":次数}
    count = {}

    # 定义匹配IP地址的正则表达式  x.x.x.x
    import re
    ip_re = r"(\d{1,3}\.){3}\d{1,3}"

    with open(web_log, mode="r") as fobj:
        for line in fobj:
            # 使用正则过滤获取客户端地址
            is_match = re.search(ip_re, line)
            if is_match:
                client_ip = is_match.group()
                if client_ip in count.keys():
                    count[client_ip] += 1
                else:
                    count[client_ip] = 1
        # 输出结果
        for ip, number in count.items():
            print("客户端地址: %s, 访问次数: %s" % (ip, number))

if __name__ == '__main__':
    webUvByRegex(r"D:\python\fileTest\access_log")
