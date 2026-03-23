# 问题链接 https://github.com/jackfrued/Python-100-Days/blob/master/Day01-20/07.%E5%88%86%E6%94%AF%E5%92%8C%E5%BE%AA%E7%8E%AF%E7%BB%93%E6%9E%84%E5%AE%9E%E6%88%98.md
import random

import util_yahier


# mark 打印出100以内的素数.素数是指除了1和它本身以外不再有其他因数的数
def test_sushu(end):
    for i in range(2, end):
        b = False  # point 布尔值是首字母大写的 False 和 True
        for j in range(2, i):
            if i % j == 0:
                b = True
                break

        if not b:
            print(i)


# 输出斐波那契数列中的前 20 个数.每一个数都是前面两数之和
def test_sum():
    # a = 2, b = 1  语法错误 point 逗号在赋值语境中有特殊含义（元组打包）； 解析器会先把 2, b 当成一个「元组表达式」，变成 a = (2, b) = 1；
    a, b = 0, 1
    for i in range(1, 10):
        c = a + b
        print(f"c is {c}")
        a, b = b, c

    # mark  更简单的写法是下面这样的
    for _ in range(20):
        a, b = b, a + b
        print("next is %d" % a)


# mark 公鸡 5 元一只，母鸡 3 元一只，小鸡 1 元三只，用 100 块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
def buy_chicken():
    # 三种🐔的价格
    a, b, c = 5, 3, 1 / 3
    # 购买的数量分别是 x,y (100-x-y)
    # 因为5x+3y+ (100-x-y*)*1/3=100
    # 解得 7x+4y = 100

    # mark 我的方法
    for x in range(20):
        for y in range(33):
            if 7 * x + 4 * y == 100:
                print(x, y)

    # mark 更通用的方法
    for x in range(0, 21):
        for y in range(0, 34):
            z = 100 - x - y
            if z % 3 == 0 and 5 * x + 3 * y + z // 3 == 100:
                print(f'公鸡: {x}只, 母鸡: {y}只, 小鸡: {z}只')
    return


# 打印乘法表
def print_multiplication_table():
    for i in range(1, 10):
        for j in range(1, i + 1):
            # mark print() 默认会在末尾添加换行符 \n
            # mark end='\t' 把结尾的换行符改成了制表符（Tab）：
            # 写法              效果
            # end = ''         不换行，直接连在后面
            # end = '\t'       结尾用制表符（对齐用）
            # end = ' '        结尾用空格
            # end = '\n'       默认，换行
            print(f'{i}×{j}={i * j}', end='\t')
        print()


# 输入两个大于 0 的正整数，求两个数的最大公约数。
def max_gongyueshu():
    print("计算两个数的最大公约数")
    input_a = input("请输入a的数值")
    while not input_a.isdigit():
        input_a = input("你输入的不是数字，请重新输入")

    a = int(input_a)

    input_b = input("再输入b的数值")
    # mark 上面用标准语法判断，这里用正则表达式判断
    while not util_yahier.is_pure_digit(input_b):
        input_b = input("你输入的不是数字，请重新输入")

    b = int(input_b)
    _min = min(a, b)
    # point range()的完整语法是range(start, stop, step)
    for i in range(_min, 0, -1):
        if a % i == 0 and b % i == 0:
            print(f"最大公约数是 {i}")
            break


# 最小公倍数
def min_gongbeishu():
    a, b = 48, 32
    for i in range(max(a, b), a * b + 1):
        if i % a == 0 and i % b == 0:
            print(f"最小公倍数是 {i}")
            break


# 双色球是由中国福利彩票发行管理中心发售的乐透型彩票，
# 每注投注号码由6个红色，红色球号码从1到33中选择，
# 1个篮球 蓝色球号码从1到16中选择。每注需要选择6个红色球号码和1个蓝色球号码
def ball_game():
    num1, num2, num3, num4, num5, num6 = random.sample(range(1, 34), 6)
    # mark 注意这里生成的随机数是包括16的
    blue = random.randint(1, 16)
    print("6个红色号码分别是", num1, num2, num3, num4, num5, num6)
    print("1个蓝色号码分别是", blue)

    fenmu = 1 * 16
    fenzi = 1 * 10000 * 1000
    for i in range(1, 34):
        fenmu *= i
    for i in range(1, 34 - 6):
        fenzi *= i
    for i in range(1, 7):
        fenzi *= i

    print(f"双色球中最大奖中一注，平均需要买{fenmu / fenzi}注", )

    return


# mark 注意啊 if必须后面需要要有空格的
if __name__ == '__main__':
    # test_sushu(10)
    # test_sum()
    # buy_chicken()
    # print_multiplication_table()
    # max_gongyueshu()
    # min_gongbeishu()
    ball_game()
