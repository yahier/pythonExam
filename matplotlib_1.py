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
    # point subplots建立坐标系
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


# 绘制饼图
def show_cake():
    print("准备打印饼图啦 ") #, np.random.rand(7, 3)
    data = np.random.randint(100, 500, 7)
    labels = ['apple', 'banan', 'peach', 'lizhi', 'shiliu', 'shanzhu', 'liulian']

    # 宽5英寸、高5英寸的正方形画布（饼图通常用正方形），每英寸120像素
    plt.figure(figsize=(5, 5), dpi=120)
    plt.pie(
        data,  # 饼图各扇区的大小
        autopct='%.1f%%',  # 自动显示百分比，保留1位小数
        radius=1,  # 饼图的半径
        pctdistance=0.8,  # 百分比到圆心的距离 0.8倍半径
        colors=np.random.rand(7, 3),  # 颜色（随机生成）
        # 分离距离
        # explode=[0.05, 0, 0.1, 0, 0, 0, 0],
        # 阴影效果
        # shadow=True,
        # 字体属性
        textprops=dict(fontsize=8, color='black'),
        # 楔子属性（生成环状饼图的关键）
        wedgeprops=dict(linewidth=1, width=0.35),
        # 标签
        labels=labels
    )
    # 定制图表的标题
    plt.title('水果销售额占比')
    plt.show()


def test_1():
    data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    fig, ax = plt.subplots(figsize=(8, 4))  # figsize设置画布大小(宽, 高)
    # ax.plot(x, y, color='blue', linestyle='-', linewidth=2, label='sin(x)')


# 简单例子
def test_2():
    # mark x 是一个包含 120 个元素的数组，从 -2π 均匀分布到 2π
    x = np.linspace(-2 * np.pi, 2 * np.pi, 120)
    y = np.sin(x)

    # point 创建画布
    plt.figure(figsize=(8, 4), dpi=120)
    # point 绘制折线图
    plt.plot(x, y, linewidth=1, marker='*', color='red')
    # 先保存图片
    plt.savefig('test.png')  # point show()方法会清空画布，如果需要保存图片，需要在show()之前调用
    # 再显示绘图
    plt.show()


def test_3():
    x = np.linspace(-2 * np.pi, 2 * np.pi, 120)
    y1, y2 = np.sin(x), np.cos(x)
    plt.figure(figsize=(8, 4), dpi=120)

    plt.subplots()  # 推荐使用subplots 创建坐标系
    # plt.subplots(3, 1, sharex=True)  # 推荐使用这种方法创建坐标系

    # 创建坐标系（第1个图）point subplot(nrows总行数, ncols总列数, index当前子图的位置（从1开始计数)
    # plt.subplot(2, 1, 1)

    plt.plot(x, y1, linewidth=2, marker='*', color='red')

    # 创建坐标系（第2个图）
    # plt.subplot(2, 1, 2)
    plt.plot(x, y2, linewidth=2, marker='^', color='blue')
    plt.show()


if __name__ == '__main__':
    # show_1()
    # show_2()
    # show_3()
     test_3()
    #show_cake()
