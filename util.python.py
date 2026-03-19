import time

import list_map


def test_datetime():
    localtime = time.localtime(time.time())
    print("年份 %d,月份 %d,日期 %d,时 %d,分 %d 秒%d" % (localtime.tm_year, localtime.tm_mon, localtime.tm_mday,
                                                        localtime.tm_hour, localtime.tm_min, localtime.tm_sec))
    print("本地时间为 :", localtime)

    # 格式化可读日期
    # %m 月份（01-12）
    # %w 星期（0-6），星期天为星期的开始0，星期六就是结束的6
    print(time.strftime("%y-%m-%d %H:%M:%S 星期:%w", time.localtime()))

    # 哈哈 import竟然可以在方法中
    import calendar
    cal = calendar.month(2026, 3)
    print("以下输出2016年1月份的日历:")
    print(cal)


def test_time():
    second = time.time()  # 时间戳 秒数
    print("当前时间戳为:", second)  # 1773888506.5291011  1773888515.6178088
    print(time.strftime("%y-%m-%d %H:%M:%S 星期:%w", time.localtime()))

    time.sleep(6)
    print("睡了6秒")
    print(time.strftime("%y-%m-%d %H:%M:%S 星期:%w", time.localtime()))


import math


# dir方法返回一个列表， 内容是模块里定义过的名字
def test_dir():
    print(dir(math))  # math is a built-in module
    print(dir(list_map))


if __name__ == '__main__':
    #test_datetime()
    # test_time()
    test_dir()
