import timeit


def test_list():
    print("\n 开始 test_list")
    list1 = ['东方', "clock", 2.23, 'john', 70.2]
    list2 = ["a无双", "z钟灵", "b白夜"]

    list2.append("d新增元素")
    # list2.insert(2, 66)  #
    list2.sort(reverse=True)  # 倒序=true,体会方法入参  todo 混合类型无法排序 
    print(list2)

    # index方法找不到元素会报错，find是字符串的方法，list没有
    print(f"list1 index  {list1.index('john', 2)}")

    if "bing" in "bingo":
        print(f"在list1中 {list1.index('')}")

    "bin".find("in")

    # point 安全的查找先判断在列表中
    if "2" in list1:
        print(f"2在list1中 {list1.index('2', 2)}")
        position2 = list1.index("2")
    else:
        print("2不在list1中")

    # print(list1[4])
    # print(list[2:4])
    # print(list1 + list2)

    # mark 初始化列表
    numbers1 = [x for x in range(1, 11)]  # 列表推导式
    numbers2 = list(range(1, 11, 3))  # 直接把 range 转成列表
    print("打印列表", numbers2)

    fruits = ['orange', 'grape', 'pitaya', 'blueberry']
    # point 遍历列表，获取索引和元素
    for index, fruit in enumerate(fruits):
        print(index, ':', fruit)


# point 元组，相当于只读的不可变列表
def test_array():
    list1 = [1, 2, 3, 4, 5, 6]

    ###添加元素
    list1.append(45)
    list1.extend([1, 2, 3, 4])

    list1.__add__([46])  # todo 错误 此方法会返回一个新列表，原列表完全不会被修改。而且此方法效率低下

    ### 按值删除
    list1.remove(1)  # 删除指定元素 匹配第一个。 如果元素不存在，会报出异常 ValueError: list.remove(x): x not in list

    # point 按索引删除
    list1.pop(2)
    del list1[2]
    deleted_value = list1.pop()  # point 根据索引位置删除（可返回被删除的元素).无参则删除最后一个
    del list1[1:3]  # point del 是 Python 关键字（不是列表方法），可以删除列表中指定索引的元素、切片范围内的元素，甚至整个列表。无返回值

    array = (1, "元祖第二项", 3, 4, 5, list1)

    # 打包
    array2 = 6, 7, 8
    # mark 解包
    a, b, c = array2
    # point 函数的特性：多个参数用逗号分隔时，会依次输出所有参数，参数之间默认用空格分隔。
    print("b,b,c分别是", a, b, c, "干啥啊")

    print(f"array[0] is {array[0]}")
    print(f"array[1:3] is {array[1:3]}")
    print(f"array + array2 is {array + array2}")

    # # value遍历
    # for value in list1:
    #     print('遍历a : %s' % value)
    #
    # # 索引遍历
    # for index in range(len(list1)):
    #     print('遍历a : %s' % list1[index])
    print('%.3f 秒' % timeit.timeit('[1, 2, 3, 4, 5, 6, 7, 8, 9]', number=10000000))  # M1 0.408 秒
    print('%.3f 秒' % timeit.timeit('(1, 2, 3, 4, 5, 6, 7, 8, 9)', number=10000000))  # M1 0.046 秒


# 集合。相当于列表去重
def test_set():
    a = {1, 2, 3, 3}  # 这是集合
    b = {}  # 这是空字典，不是集合
    s = {1, 2, 3}
    list = [1, 2, 3, 3]
    s = set(list)
    print(str(type(a)) + "" + str(type(b)))
    print("s=" + str(s))


from typing import List


def test_convert():
    # 这是泛型的写法，但运行也不会报错，真正的类型检查需要依赖 mypy 这类静态分析工具在代码运行前完成
    my_list: List[int] = [1, "bingo", 3, 4]
    ###mark 列表转换成元祖
    my_list = [1, "bingo", 3, 4]
    # 使用 tuple() 函数转换
    my_tuple = tuple(my_list)
    print(my_tuple)  # 输出: (1, 2, 3, 4)
    print(type(my_tuple))  # 输出: <class 'tuple'>

    ###mark 元祖转换成列表
    my_tuple = (10, "hello", 30)
    # 使用 list() 函数转换
    my_list = list(my_tuple)
    print(my_list)  # 输出: [10, 20, 30]
    print(type(my_list))  # 输出: <class 'list'>


# 字典
def test_map():
    my_dict = dict()

    dict = {}
    dict['one'] = "This is one"
    dict[2] = "This is two"

    tinydict = {'name': 'runoob', 'code': 6734, 'dept': 'sales'}

    for key, value in tinydict.items():
        print(f" 遍历字典 {key}: {value}")


    # mark 带默认值的获取方法
    dict.get("one", "bingo")

    print(dict['one'])  # 输出键为'one' 的值
    print(dict[2])  # 输出键为 2 的值
    print(tinydict)  # 输出完整的字典
    print(tinydict.keys())  # 输出所有键
    print(tinydict.values())  # 输出所有值


if __name__ == '__main__':
    test_list()
# test_convert()
# test_array()
# test_map()
# test_set()
