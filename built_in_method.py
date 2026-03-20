# point 内置方法试验

def test_all():
    print("")


def data():
    # NOTE: 这里的魔法数字 42 来源于业务部门的特定要求
    print("开始试验数据相关")
    print(bool(-1))  # 只有''和0是false,其他都是true
    print(str(1.5))

    list1 = [1, 2, 3, 4]
    print(all(list1))

    print("bingo".startswith("he"))
    print(f"长度是{len("bingo")}")
    len(list1)
    type1 = type("")  # point type方法
    print(f"{type1}类型的方法有{dir(type1)}")  # point dir方法 列出对象的所有属性和方法，调试神器。
    print(f"eval执行字符串表达式 并返回值 {eval("4+6")}")  # point eval

    iterator_1 = range(5)
    iterator_2 = range(3, 6)  # point 返回的是一个可迭代对象（类型是对象），而不是列表类型
    print(f"type is {type(iterator_2)} 数据 {iterator_2}")  # mark 打印结果是 type is <class 'range'> 数据 range(0, 5)

    # 这才是列表，直接range出来的只是可迭代对象
    list4 = [i + 2 for i in range(5)]


for i in range(5):
    print("range循环 value = " + str(i))

if __name__ == "__main__":
    data()
