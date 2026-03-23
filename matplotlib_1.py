import matplotlib.pyplot as plt
import numpy as np


# 绘制一个正弦函数图像。
def show_1():
    # 1. 准备数据
    x = np.linspace(0, 2 * np.pi, 100)  # 在0到2π之间生成100个点
    y = np.sin(x)  # 计算对应的正弦值

    # 2. 创建画布和坐标轴
    fig, ax = plt.subplots(figsize=(8, 4))  # figsize设置画布大小(宽, 高)

    # 3. 绘制图形
    ax.plot(x, y, color='blue', linestyle='-', linewidth=2, label='sin(x)')

    # 4. 添加标题和坐标轴标签
    ax.set_title('基础正弦曲线图', fontsize=14)
    ax.set_xlabel('x (弧度)', fontsize=12)
    ax.set_ylabel('sin(x)', fontsize=12)

    # 5. 添加图例
    ax.legend()

    # 6. 显示图形
    plt.show()


# 生成柱形图
def show_2():
    categories = ['A', 'B', 'C', 'D']
    values = [10, 25, 15, 30]
    fig, ax = plt.subplots()
    ax.bar(categories, values, color='skyblue')
    plt.show()


# 散点图 (Scatter Plot)
def show_3():
    x = np.random.rand(50)
    y = np.random.rand(50)
    fig, ax = plt.subplots()
    ax.scatter(x, y, color='red', marker='o')  # marker定义点的形状
    plt.show()


def show_4():
    # 1. 准备数据
    matrix = np.random.randint(0, 100, (3, 3))  # 3x3 的随机整数矩阵

    # 2. 创建画布
    fig, ax = plt.subplots(figsize=(6, 6))

    # 3. 使用 imshow 显示矩阵
    # cmap='hot' 使用热图配色
    # interpolation='nearest' 保持像素清晰，不进行平滑处理
    im = ax.imshow(matrix, cmap='hot', interpolation='nearest')

    # 4. 添加颜色条 (Colorbar)
    plt.colorbar(im, label='数值大小')

    # 5. (可选) 在每个格子里手动添加数值文本
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # 在坐标 (j, i) 处写入文本
            # ha='center' 水平居中, va='center' 垂直居中
            text_color = 'white' if matrix[i, j] > 50 else 'black'  # 根据背景深浅调整文字颜色
            ax.text(j, i, str(matrix[i, j]), ha='center', va='center', color=text_color)

    plt.title('Matplotlib imshow 矩阵显示')
    plt.show()



def test_1():
    data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    fig, ax = plt.subplots(figsize=(8, 4))  # figsize设置画布大小(宽, 高)
    # ax.plot(x, y, color='blue', linestyle='-', linewidth=2, label='sin(x)')


if __name__ == '__main__':
    # show_1()
    #show_2()
    # show_3()
    show_4()
