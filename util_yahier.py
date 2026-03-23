import time
import timeit

import list_map
import re


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


# point 正则表达式判断是否全部是数字
# mark 正则规则：^[0-9]+$ 或等价的 ^\d+$
# mark ^：匹配字符串开头（确保前面无其他字符）
# mark \d：等价于 [0-9]，匹配单个数字字符
# mark +：匹配前面的规则「至少 1 次」（避免空字符串）
# mark $：匹配字符串结尾（确保后面无其他字符）
# mark 结合 re.fullmatch() 函数（最简洁，直接判断整个字符串是否匹配）
def is_pure_digit(input_str):
    """判断输入字符串是否为纯数字（正整数/0）"""
    # 正则匹配：从头到尾全是数字，且至少1位
    pattern = r'^\d+$'  # point r 是原始字符串（raw string） 的标识, 它会告诉 Python 解释器：不要处理字符串中的反斜杠 \，直接按字面意思解析
    # fullmatch 等价于用 ^ 和 $ 包裹正则，判断整个字符串匹配
    result = re.fullmatch(pattern, input_str)
    # 匹配成功返回 True，否则 False
    return bool(result)


def test_timeit():
    print('%.3f 秒' % timeit.timeit('[1, 2, 3, 4, 5, 6, 7, 8, 9]', number=10000000))
    print('%.3f 秒' % timeit.timeit('(1, 2, 3, 4, 5, 6, 7, 8, 9)', number=10000000))

    setup_code = '''def add(a, b): return a + b'''  # point 三引号'''才能得到Python代码文本

    # python中，''和""的语法意义几乎完全相同的，官方文档倾向于用单引号
    word = 'he said "i went to dinner"'  # 内部有双引号，则外面用单引号
    word = "he said 'i went to dinner'"  # 内部有单引号，则外面用双引号
    print(f"eval执行字符串表达式 并返回值 {eval("4+6")}")  # point eval

    # 测试代码：调用函数
    stmt_code = 'add(10, 20)'
    # mark:  setup 测试前的准备代码（比如导入模块、定义变量 / 函数），默认 pass
    # mark:  stmt (statement缩写)	要测试的代码（字符串 / 可调用对象），默认是 pass（空代码）
    cost = timeit.timeit(setup=setup_code, stmt=stmt_code, number=1000000)  # point
    print(f"执行100万次add函数耗时：{cost:.6f} 秒")

    # value = timeit.timeit(stmt=stmt_code, setup=setup_code, number=1000000)
    # print('%.3f 秒' % value)


if __name__ == '__main__':
    # test_datetime()
    # test_time()
    # test_dir()
    test_timeit()
