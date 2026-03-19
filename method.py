# 默认参数
from main import test_main
#import main

def test_1(name, hobby="playing"):
    string = "i am %s,i like %s" % (name, hobby)
    print(string)


# 可写函数说明
def test_2(arg1, *vars):
    print("测试 不定长参数")
    print(arg1)
    for var in vars:
        print(var)
    return


# 匿名函数 lambda [arg1 [,arg2,.....argn]]:expression
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
