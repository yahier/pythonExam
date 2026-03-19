# 这是一个示例 Python 脚本。

# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 ⌘F8 切换断点。


def test_array():
    a = [1, 2, 3]
    b = [4, 5, 6, 8, 10]

    for item in zip(a, b):
        print(item)


b = 2
bingo = "who"
def test_main():
    print("我是testMain")


def change_int(a):
    a = 10


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('世界')
    test_array()
    change_int(b)
    print("b is %d" %b)

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
