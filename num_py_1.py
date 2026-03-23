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
    # 一维数组
    arr1d_1 = np.array([1, 2, 3, 4, 5])
    arr1d_2 = arr1d_1 * 2
    arr1d_3 = np.array([6, 7, 8, 9, 10])
    print(arr1d_2)

    # 二维数组（矩阵）
    # arr2d = np.array([[1, 2, 3], [4, 5, 6]])
    return


# 二维数组(矩阵)
def test_2d():
    # 创建二维数组（矩阵）
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])

    # 矩阵加法
    print(a + b)  # [[ 6  8], [10 12]]

    # 矩阵乘法（点积）todo 忘了矩阵乘法了
    print(np.dot(a, b))  # [[19 22], [43 50]]

    # 矩阵转置
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
    print(np.arange(10))  # [0 1 2 3 4 5 6 7 8 9]

    # 生成 3x3 的全零矩阵
    print(np.zeros((3, 3)))

    # 生成 2x2 的随机数矩阵（0-1 之间）
    print(np.random.random((2, 2)))


if __name__ == '__main__':
    test_2d()
    # print(dir(np))
