import numpy as np


# point NumPy 是 Python 中最核心的数值计算库（全称 Numerical Python），它的核心是提供了高性能的多维数组（ndarray） 和一套针对数组的数学运算工具，是数据分析、机器学习、科学计算的「基石」。
# point 简单比喻：如果把Python自带的列表（list）比作「普通购物袋」，那NumPy的数组就是「专业工具箱」—— 更高效、更适合做数值计算，还能直接做矩阵 / 向量运算。
# point NumPy的核心特点
# point 1、高性能数组：比Python原生列表快数十倍（底层用C实现，避免了Python循环的性能损耗）；
# point 2、多维支持：轻松创建一维（向量）、二维（矩阵）、三维及以上数组；
# point 3、向化运算：无需写for 循环，直接对整个数组做加减乘除、矩阵乘法等；
# point 4、丰富的数学函数：内置线性代数、傅里叶变换、随机数生成等功能。

# 一维数组
def test1():
    print("测试 test1 方法")
    # 一维数组
    arr1d_1 = np.array([1, 2, 3, 4, 5])
    arr1d_2 = arr1d_1 * 2
    print(f"arr1d_1 is {arr1d_1}")
    print(f"arr1d_2 is {arr1d_2}")

    # mark  NumPy 数组支持直接做数学 / 条件运算
    print(f" 判断方法测试1 {type(arr1d_1 >= 2)}    {(arr1d_1 >= 2).all()}")
    print(f" 判断方法测试2   {arr1d_1.all()}")

    array4 = np.arange(0, 10, 3)  # point 0到10  步长为3  输出[ 0,3,6,9]
    print(f" arange方法创建 arr1d_4 is {array4}")
    # 二维数组（矩阵）
    # arr2d = np.array([[1, 2, 3], [4, 5, 6]])
    return


# 二维数组(矩阵)
def test_2d():
    print("测试 test_2d方法")
    # 创建二维数组（矩阵）
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])

    print("取二维数组的第二行 ", a[1])  # mark 取值
    print("取二维数组的第二行第二列", a[1][1])  # mark 取值
    a[1] = [9, 0]  # mark 很简单的就给某一项赋值了
    print(f" 看看类型  type1 is {type(a[1])}   type2 is {type(a[1][1])}")
    print("重新赋值后 取二维数组的第二行第二列", a[1][1])  # mark 取值

    if a[1][1] == 0:  # point 为什么这里会相等呢  ==只看值;is才看类型+内存
        print("二维数组和int值比较  相等")
    else:
        print("二维数组和int值比较 不相等")

    # 矩阵加法
    print(a + b)  # [[ 6  8], [10 12]]

    # 矩阵乘法（点积）todo 忘了矩阵乘法了
    print("测试 矩阵乘法")
    print(np.dot(a, b))  # [[19 22], [43 50]]

    # point 矩阵转置(行列互换)  A(m,n) = B(n,m)
    print("测试 矩阵转置")
    print(a.T)  # [[1 3], [2 4]]


# mark 快速的数据统计分析
def test_data_compute():
    data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    # 计算平均值、最大值、求和
    print(data.mean())  # 5.0（整体均值）
    print(data.max(axis=0))  # [7 8 9]（按列取最大值）
    print(data.sum(axis=1))  # [6 15 24]（按行求和）


# mark 生成特定规律的数组
def test_create():
    # 生成 0-9 的整数数组
    nd1 = np.arange(10)

    print(nd1)  # [0 1 2 3 4 5 6 7 8 9]
    print("一维数组的type", type(nd1), "size=", nd1.size, "shape is", nd1.shape)

    # 生成 3x3 的全零矩阵
    print(np.zeros((3, 3)))

    nd2 = np.ones((2, 3))  # 两行三列全是1
    print("2维数组的type", type(nd2), "shape is", nd2.shape)

    np.full(2,4)
    np.full((2, 3), 5)  # point 两行三列全是5。爱这样的标准通用方法
    print(nd2.size)

    # 生成 2x2*4 的三维随机数矩阵（0-1 之间）
    print("测试random方法", np.random.random((2, 2, 4)))

    random23 = np.random.rand(2, 3)  # mark 生成2行3列的二维NumPy数组，每个元素都是一个大于等于 0.0 且小于 1.0 的随机小数。

    print("测试rand方法", random23)


    print("测试randint方法", np.random.randint(0, 9, 4)) #mark  创建一维随机数组
    scores = np.random.randint(60, 101, (5, 3)) #mark 创建二维随机数组


def test_temp_0426():
    # array = np.eye(3)  # 3阶单位矩阵(左上到右下的对角线全是1，其他都是0)
    array = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"临时测试方法 test_temp\n{array}")
    print(f"维度是{array.ndim}  数量是{array.size} 形状是{array.shape}  数据类型是{array.dtype} 数组转置 {array.T}")

    arr = np.array([1, 2, 3, 4, 5, 6, 7], )
    # print(f"取值[0] is {arr[0]}")  # 第一个元素 → 1
    # print(f"按索引取值 {arr[1:6:3]}")  # 和string一模一样 太棒了
    print(f"尝试倒序 {arr[::-1]}  另外一种倒序{list(reversed(arr))}")  # [-1]取的是最后一个 这里是::-1表示从头到尾以步长-1进行切片，即反向读取，倒序

    print(f"第一列的所有元素 {array[:, 0]}")  # 取第一列所有元素
    print(f"第一行的所有元素 {array[1, :]}")  # 取第2行所有元素
    print(f"取子切片 {array[1:2, :]}")  # 区索引为1的行(第二行)，列全取

    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    a + b  # 加法 → [5 7 9]
    a - b
    a * b  # 对应元素相乘（不是矩阵乘法）
    a / b
    a ** 2  # 平方 → [1 4 9]
    np.sqrt(a)  # 开方
    np.exp(a)  # 指数


if __name__ == '__main__':
    #test1()
    # test_2d()
    test_create()
# print(dir(np))
# test_temp_0426()
