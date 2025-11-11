# 用户访问量      客户端地址: x.x.x.x    访问次数: xxxxx


def webUv(web_log):

    # 规划字典，统计次数  {"客户端地址":次数}
    count = {}

    with open(web_log, mode="r") as fobj:
        for line in fobj:
            # 获取客户端地址
            client_ip = line.split()[0]
            if client_ip != "::1":
                if client_ip in count.keys():
                    count[client_ip] += 1
                else:
                    count[client_ip] = 1
        # 输出结果
        for ip, number in count.items():
            print("客户端地址: %s, 访问次数: %s" % (ip, number))

if __name__ == '__main__':
    webUv(r"D:\project1110\fileTest\access_log")

