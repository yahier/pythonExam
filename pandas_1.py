# Pandas 是 Wes McKinney 在2008年开发的一个强大的分析结构化数据的工具集。Pandas 以 NumPy 为基础（实现数据存储和运算），
# 提供了专门用于数据分析的类型、方法和函数，对数据分析和数据挖掘提供了很好的支持；同时 pandas 还可以跟数据可视化工具 matplotlib 很好的整合在一起，非常轻松愉快的实现数据可视化呈现。

# Pandas 核心的数据类型是Series（数据系列）、DataFrame（数据窗/数据框），分别用于处理一维和二维的数据，
# 除此之外，还有一个名为Index的类型及其子类型，它们为Series和DataFrame提供了索引功能。
# 日常工作中DataFrame使用得最为广泛， 因为二维的数据结构刚好可以对应有行有列的表格。
# Series和DataFrame都提供了大量的处理数据的方法，数据分析师以此为基础，可以实现对数据的筛选、合并、拼接、清洗、预处理、聚合、透视和可视化等各种操作。

import numpy as np
import pandas as pd  # 命令行安装 pip3 install pandas


def test_1():
    # point Series类型的内部结构包含了两个数组，其中一个用来保存数据，另一个用来保存数据的索引

    # mark Series方法建立 一维带标签的数组（一行 / 一列数据），参数解析
    # 1、data参数非常强大，支持这些类型：列表、数组、字典、单个值、numpy 数组
    # 2、index（索引 / 行标签）.给每一行数据起名字（标签），方便查找;必须和 data 长度一样
    # 3、 dtype（指定数据类型）常用：int, float, str, bool
    # 4、name（给 Series 起名字）;给这一列数据起个名字，将来转 DataFrame 时会变成列名

    # 通过列表或数组创建Series对象
    ser1 = pd.Series(name="数据报表", data=[120, 380, 250, 360], index=['一季度', '二季度', '三季度', '四季度'])
    ser1 = ser1 + 10  # 数据项 每一个都+10
    print("Series方法得到的类型是：", type(ser1))
    print("\n第一个对象\n", ser1)

    # 通过字典创建Series对象
    ser2 = pd.Series(data={'一季度': 320, '二季度': 180, '三季度': 300, '四季度': 405})
    print("\n第2个对象\n", ser2)

    print("取值测试", ser2['二季度'], ser2.iloc[1])
    # print("取值测试", ser2[0])  # 当前版本出现问题，因为索引不是整数

    ser3 = ser1 + ser2  # market 索引相同的相加合并
    ser3 = ser3.sort_values(ascending=False)  # ascending升序 point 调用排序后 需要重新赋值 原列表没有排序
    # ser3 = ser3.sort_index(ascending=False) #point 和以上一样
    print("\n第3个对象\n", ser3)

    ser4 = pd.Series(data=[1, 2, 3, 4])
    ser3.sort_values()


def test_compute():
    print("\n开始 test_compute")
    ser2 = pd.Series({'一季度': 320, '二季度': 180, '三季度': 300, '四季度': 405})
    print("计数", ser2.count())  # 计数
    print("求和", ser2.sum())  # 求和
    print("平均", ser2.mean())  # 求平均
    print("中位数", ser2.median())  # 找中位数
    print("最大", ser2.max())  # 找最大
    print("最小", ser2.min())  # 找最小
    print("标准差", ser2.std())  # 求标准差
    print("方差", ser2.var())  # 求方差


if __name__ == '__main__':
    test_1()
    test_compute()
