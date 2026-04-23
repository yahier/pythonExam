# 默认参数
from main import test_main


# import main

def test_1(name, hobby="playing"):
    string = "i am %s,i like %s" % (name, hobby)
    print(string)


# 可写函数说明
# point *用于接收任意数量的位置参数， 会把传入的多个位置参数打包成一个元组（tuple）
def test_2(arg1, *vars):
    print("测试 不定长参数")
    print(arg1)
    for var in vars:
        print(var)
    return


# point ** 会把传入的多个关键字参数（key=value 形式）打包成一个字典（dict），让函数能接收不确定数量的关键字参数（也叫「可变关键字参数」）。
def print_info(**kwargs):
    print("kwargs的类型：", type(kwargs))  # 输出：<class 'dict'>
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# point 匿名函数 lambda [arg1 [,arg2,.....argn]]:expression
sum = lambda arg1, arg2: arg1 + arg2

if __name__ == '__main__':
    # 命名调用
    test_1(hobby="swim", name="bingo")
    # 超厉害的不定长参数
    test_2("1", [2, 3])
    test_2("郭富城", "动起来", "为新的力量喝彩")

    print(sum(12, 21))
    bingo = "我是谁"
    test_main()

    print("双* 测试 可变关键字参数")
    print_info(name="张三", age=20)
    print_info(city="北京", job="程序员", salary=20000)
