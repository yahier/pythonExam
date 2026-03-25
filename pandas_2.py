import numpy as np
import pandas as pd


# 仿照73.深入浅出pandas-2 https://github.com/jackfrued/Python-100-Days/blob/master/Day66-80/73.%E6%B7%B1%E5%85%A5%E6%B5%85%E5%87%BApandas-2.md
# mark 如果使用 pandas 做数据分析，那么DataFrame一定是被使用得最多的类型，它可以用来保存和处理异质的二维数据。
# mark 这里所谓的“异质”是指DataFrame中每个列的数据类型不需要相同，这也是它区别于 NumPy 二维数组的地方。
# mark DataFrame提供了极为丰富的属性和方法，帮助我们实现对数据的重塑、清洗、预处理、透视、呈现等一系列操作。

def test_dataframe_1():
    # mark 通过二维数组创建DataFrame对象
    scores = np.random.randint(60, 101, (5, 3))
    courses = ['语文', '数学', '英语']
    stu_ids = np.arange(1001, 1006)
    df1 = pd.DataFrame(data=scores, columns=courses, index=stu_ids)
    print("第一个对象\n", df1)

    # mark 通过字典创建DataFrame对象
    scores = {
        '语文': [62, 72, 93, 88, 93],
        '数学': [95, 65, 86, 66, 87],
        '英语': [66, 75, 82, 69, 82],
    }
    stu_ids = np.arange(1001, 1006)
    df2 = pd.DataFrame(data=scores, index=stu_ids)
    print("\n第二个对象\n", df2)


def test_read_csv():
    df3 = pd.read_csv('file/2018年北京积分落户数据.csv', index_col='id')
    print("\n读取csv文件\n", df3)


# mark 读取xlsx文件需要安装 pandas 和 openpyxl
# 命令行安装openpyxl：pip3 install pandas openpyxl
def test_read_xlsx():
    df4 = pd.read_excel('file/2022年股票数据.xlsx', sheet_name='AMZN', index_col='Date')
    print("\n读取xlsx文件\n", df4)


def write_xlsx():
    # 1. 分别读取两个Excel文件
    df1 = pd.read_excel('file/江湖门派录.xlsx')
    df2 = pd.read_excel('file/江湖名人录.xlsx')

    # point 使用 concat方法 进行纵向合并(行数相加)
    # ignore_index=True 会重置合并后的索引，从0开始重新编号
    df_combined = pd.concat([df1, df2], ignore_index=True)

    # 3. 将合并后的数据保存到一个新的Excel文件中
    df_combined.to_excel('file/new_combined_vertical.xlsx', index=False)
    print("\n文件合并完成\n")


def merge():
    df1 = pd.read_excel('file/江湖门派录.xlsx')
    df2 = pd.read_excel('file/江湖名人录.xlsx')

    # point how代表了合并两张表的方式，有left、right、inner、outer四个选项, 我觉得outer最好用
    # mark 还有一个重要参数 on='dno' 代表了基于哪个列实现表的合并，相当于 SQL 表连接中的连表条件;
    # mark 如果左右两表对应的列列名不同，可以用left_on和right_on参数取代on参数分别进行指定
    df_combined = pd.merge(df1, df2, how='outer')
    df_combined.to_excel('file/merge_.xlsx', index=False)


if __name__ == '__main__':
    # test_dataframe_1()
    # test_read_xlsx()
    # write_xlsx()
    merge()
