import math
from random import choice, random, randrange

import main


# todo 字符串是不可变的，所有操作都会返回新字符串。
def string_test():
    string = "hello world"
    # 剪裁获取部分
    str = string[0:5]

    print(str)
    str2 = string * 3
    print(str2)

    # %s是一个占位符，它相当于一个“坑”，暂时占据一个位置，等着后面填入一个字符串（或者能被转换成字符串的任何数据，比如数字、变量等）
    # %：这是格式化操作符。它告诉 Python：“嘿，看这里！把前面字符串里的占位符，用后面这个值替换掉
    print('占位符 格式化 : %s' % 100)

    # todo f 是 f-string（格式化字符串字面量）的标识符。把花括号 {} 里的内容替换成实际的数值。”
    name = "bingo"
    print(f"异常信息: {name}")

    # 三引号
    str4 = ''' 这是一个三引号字符串
    保持原本的所有格式，包括换行
    包括字符串内的特殊符号"$/ 这样'''
    print(str4)

    str5 = "   hello bingo  "
    str5 = str5.lstrip().rstrip()

    print("精简字符串" + str5)
    print("设置宽度" + str5.center(40) + "-end")

    # python中，''和""的语法意义几乎完全相同的，官方文档倾向于用单引号
    word = 'he said "i went to dinner"'  # 内部有双引号，则外面用单引号
    word = "he said 'i went to dinner'"  # 内部有单引号，则外面用双引号

    count = "bingoo".count("o")
    print("出现了o的次数", count)
    print(f"出现了{count}次o")
    print("出现了%d次" % count)

    # point  ==判断内容是否相等，is判断是否同一个对象。
    name1 = "bingo"
    name2 = "bingo"
    print(f"name1和name2 内容相等 {name1 == name2}")
    # point 根据Python的字符串不可变特性，每一个str都的新的，根据这个理论，这两个字符串应该不是同一个，但是我这里执行的结果 竟然是True
    # point 这里得到True,是Python内部优化机制导致的，这个机制叫做字符串驻留（String Interning）。但在不同版本中的实现可能不同
    print(f"name1和name2 是同一个对象吗 {name1 is name2}")


# 计算相关
def test_compute():
    print()
    print("test_compute 测试计算相关的开始咯")
    a = 4 ** 3  # 4的3次方
    b = 9 / 5  # 4.5
    c = 9 // 5  # 2 向下取整
    d = 9 % 4  # 1 取余数
    print(str(a) + "  " + str(b) + " " + str(c) + " " + str(d))

    m = 4.5
    n = int(m)  # 浮点变整形 值为4
    p = float(4)  # 整型变浮点4.0

    print("测试sum方法1 sum([1, 2, 3])", sum([1, 2, 3]))
    print("测试sum方法2  sum(range(101))", sum(range(101)))


# 条件语句
def test_condition():
    print("\n开始测试 test_condition")
    a = 0
    if a:  # 0和null为false,其他全部是true  python不喜欢{}
        print("a is true")
    else:
        print("a is false")

    # 留意elif or
    b = 1
    if b > 1 or b > 4:
        print("b is greater than 1")
    elif b < 1:
        print("b is less than 1")
    else:
        print("b equal 1")

    for a in range(5, 10):
        print("for循环", a)


def test_pass():
    for a in range(1, 6):
        if a == 3:
            pass
            # pass语句 只用来占位，不做任何操作。下面这句结束了都会照常执行
            print("test_pass 结束了")
        else:
            print("test_pass value=", a)


# point 三种格式化的输出,第二种是最优雅的
def test_print():
    print("My name is %s and age is %d" % ("bingo", 21))
    print(f"-1转换成Boolean {bool(-1)}")  # 只有''和0是false,其他都是true
    # point 以下这些都视为False  -> None,0,0.0,"" '' [] () {}
    print("1.5转换成str", str(1.5))


# 数学相关
def test_math():
    print()
    print("test_math 测试数学相关的开始咯")
    print("最小值是 %d" % (min(4, 2, 5)))
    print("最小值是 %s" % (min("5", "bingo", "yahier", "cindy")))

    max(3, 2)
    abs(-3)

    # mark math.floor向下取整
    print("math.floor(6.6) is ", math.floor(6.6))  # 得到 6  地板
    print("math.ceil(4.4) is ", math.ceil(4.4))  # 得到 5    天花板
    print("round(6.6) is ", round(6.6))  # 得到 7    四舍五入
    print("int(6.6) is ", int(6.6))  # 得到 6

    # math是模块，下面这样是引用自己的模块，其实就是Python文件名
    main.print_hi("PyCharm")  # 模块引入

    choice([1, 2, 3])  # 从列表中随机取一个数
    random()  # 随机生成下一个实数，它在[0,1)范围内。
    randrange(1, 10, 5)  # 从1到10中随机取一个数


# 字符串相关
def test_str():
    print("\ntest_str测试字符串相关的开始咯")
    var1 = '123456789'

    # 字符串剪裁
    print("var1[0]: ", var1[0:9:3])  # mark: 三个参数分别表示 起始位置:结束位置(不包含):步长
    print("var2[1:5]: ", var1[1:5])

    # 字符串是否包含
    print("测试in方法", "236" in var1)  # mark: in方法的内部就是调用了__contains__
    print(var1.__contains__("234"))
    print(var1.find("0234"))  # find是str独有的方法，list都没有

    print(f"float('1') is {int('1')}")
    print(f"float('1.5') is {float('1.5')}")
    print(f"str(1.88) is {str(1.88)}")


# 测试解包
def test_unpack():
    print("\n 解包方法test_unpack")
    # 1. 列表解包
    fruits = ["apple", "banana", "cherry"]
    a, b, c = fruits
    print(f"a is {a} b is {b} c is {c}")

    # 2. 元组解包
    coordinates = 10, 20
    x, y = coordinates
    print(f"元祖解包 x is {x} ,y is {y}")  # 输出: 10

    # 3. 字符串解包 (按字符拆分)
    name = "ABC"
    c1, c2, c3 = name
    print(f"字符串解包 c1 is {c1} c2 is {c2} c3 is {c3}")  # 输出: A

    # point 解包时两边元素的个数要相等，或者可以使用星号 * 来捕获“剩余”的所有元素
    numbers = [1, 2, 3, 4, 5, 6]
    first, *rest = numbers
    print(f"解包 用*r表示剩余所有 first is {first}, rest is {rest}")  # 输出: 1

    # 2. 获取首尾，收集中间
    start, *middle, end = numbers
    print(f"start is {start} middle is {middle}")

    person = {"name": "Bob", "age": 30}
    for key, value in person.items():
        print(f" 遍历字典 {key}: {value}")


if __name__ == '__main__':
    test_math()
    string_test()
    test_compute()
    test_pass()
    test_condition()
    test_str()
    test_unpack()
