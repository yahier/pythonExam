import math
from random import choice, random, randrange

import main


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

    # 三引号
    str4 = ''' 这是一个三引号字符串
    保持原本的所有格式，包括换行
    包括字符串内的特殊符号"$/ 这样'''
    print(str4)

    str5 = "   hello bingo  "
    str5 = str5.lstrip().rstrip()

    print("精简字符串" + str5)
    print("设置宽度" + str5.center(40) + "-end")

    #python中，''和""的语法意义几乎完全相同的，官方文档倾向于用单引号
    word = 'he said "i went to dinner"' #内部有双引号，则外面用单引号
    word = "he said 'i went to dinner'" #内部有单引号，则外面用双引号


# 计算相关
def test_compute():
    a = 4 ** 3  # 4的3次方
    b = 9 / 2  # 4.5
    c = 9 // 4  # 2 向下取整
    d = 9 % 4  # 1 取余数
    print(str(a) + "  " + str(b) + " " + str(c) + " " + str(d))

    m = 4.5
    n = int(m)  # 浮点变整形 值为4
    p = float(4)  # 整型变浮点4.0


# 条件语句
def test_condition():
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
        print(a)


def test_pass():
    for a in range(1, 4):
        if (a == 3):
            pass
            # break
            print("结束了")  # pass也将整个循环跳过了。和break的区别是，pass会打印本句print，但break不会打印
        else:
            print(a)


# 数学相关
def test_math():
    print("最小值是 %d" % (min(4, 2, 5)))
    print("最小值是 %s" % (min("bingo", "yahier", "cindy")))

    max(3, 2)
    abs(-3)
    math.ceil(4.6)
    math.floor(6.6)  # math是模块，下面这样是引用自己的模块，其实就是Python文件名

    main.print_hi("PyCharm")  # 模块引入

    choice([1, 2, 3])  # 从列表中随机取一个数
    random()  # 随机生成下一个实数，它在[0,1)范围内。
    randrange(1, 10)  # 从1到10中随机取一个数


# 字符串相关
def test_str():
    var1 = '123456789'

    # 字符串剪裁
    print("var1[0]: ", var1[0])
    print("var2[1:5]: ", var1[1:5])

    # 字符串是否包含
    print("236" in var1)  #
    print(var1.__contains__("234"))
    print(var1.find("0234"))

    print("My name is %s and age is %d" % ("bingo", 21))


if __name__ == '__main__':
    # test_math()
    string_test()
# test_compute()
# test_pass()
# test_str()
