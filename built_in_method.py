# point 内置方法试验

def data():
    # NOTE: 这里的魔法数字 42 来源于业务部门的特定要求
    print("开始试验数据相关")
    print(f"-1转换成Boolean {bool(-1)}")  # 只有''和0是false,其他都是true
    print("1.5转换成str", str(1.5))

    list1 = [1, 2, 3, 4]
    print("测试all(list)方法 所有的item都为true时，列表all方法才为true", all(list1))

    print("bingo".startswith("he"))
    print(f"长度是{len("bingo")}")
    len(list1)
    type1 = type("")  # point type方法
    print(f"{type1}类型的方法有{dir(type1)}")  # point dir方法 列出对象的所有属性和方法，调试神器。
    print(f"eval执行字符串表达式 并返回值 {eval("4+6")}")  # point eval

    # 这才是列表，直接range出来的只是可迭代对象
    list4 = [i + 2 for i in range(5)]


# for i in range(5):
#     print("range循环 value = " + str(i))


# point 三种格式化的输出,第二种是最优雅的
def test_print():
    print("最小值是 %d" % (min(4, 2, 5)))
    print(f"-1转换成Boolean {bool(-1)}")  # 只有''和0是false,其他都是true
    print("1.5转换成str", str(1.5))




# 测试range方法
def test_range():
    print()
    print("测试range方法 test_range")
    # point range(1, 20, 4)：range返回的是一个规则，这里是告诉计算机“记住这个规则：从1开始，每次加4，直到20”。它不占什么内存，但你看不到具体数字
    # point list(range(1, 20, 4))：告诉计算机“请按照这个规则，把所有数字都算出来，放进一个盒子里（列表）
    print(f"range(1,20,4) {range(1, 20, 4)}")  # mark 输出的是 range(1, 20, 4),因为 range() 函数返回的是一个惰性序列对象（range 对象），而不是一个列表。
    print(f"range(1,10,5) {list(range(0, 10, 5))}")  # mark 输出的是 [1, 5, 9, 13, 17],三个参数分别是开始位置，结束位置，步长

    range_2 = range(3, 6)  # point 返回的是一个可迭代对象（类型是对象），而不是列表类型
    print(f"type is {type(range_2)} 数据 {range_2}")  # mark 打印结果是 type is <class 'range'> 数据 range(0, 5)


if __name__ == "__main__":
    data()
    test_range()
