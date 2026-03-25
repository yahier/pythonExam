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
    arr1d_3 = np.array([6, 7, 8, 9, 10])
    print(arr1d_2)

    array3 = np.arange(0, 20, 2)  # [ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18]
    print(array3)
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
    print("重新赋值后 取二维数组的第二行第二列", a[1][1])  # mark 取值
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

    np.full((2, 3), 5)  # point 两行三列全是5。爱这样的标准通用方法
    print(nd2.size)

    # 生成 2x2*4 的三维随机数矩阵（0-1 之间）
    print("测试random方法", np.random.random((2, 2, 4)))

    random23 = np.random.rand(2, 3)  # mark 生成2行3列的二维NumPy数组，每个元素都是一个大于等于 0.0 且小于 1.0 的随机小数。

    print("测试rand方法", random23)

    print("测试randint方法", np.random.randint(0, 9, 4))


if __name__ == '__main__':
    # test1()
    # test_2d()
    test_create()
    # print(dir(np))
