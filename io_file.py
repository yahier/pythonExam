# Python 文件I/O 参考 https://www.runoob.com/python/python-files-io.html
import os
from pathlib import Path


# input 从标准输入读入一行文本，默认的标准输入是键盘
def test_input():
    content = input("请输入")
    print(content)


def test_write():
    # open(file_name [, access_mode][, buffering])
    # mode有非常多种 比如只读r(默认模式)，写入w(每次都覆盖写入，文件不存在则创建)，追加a(内容追加，文件不存在则创建)
    # mode r+ 打开一个文件用于读写。文件指针将会放在文件的开头。
    fo = open("foo.txt", "a")
    fo.write("\n超级塞牙人的能量级别相当于星球级别")
    # content = fo.read()
    # print("content is %s" % content)
    fo.close()


file_name = "foo.txt"


def test_read_all_content():
    # 用检查文件的方式 检查文件是否存在
    file = Path(file_name)
    if not file.exists() or not file.is_file():
        print('文件不存在')
        return

    file = open(file_name, 'r', encoding='utf-8')
    # 这是最符合 Python 风格（Pythonic）的写法。它不会一次性将整个文件加载到内存中，而是每次只读取一行，非常适合处理大文件。
    for line in file:
        # line.strip() 用于去除行尾的换行符和首尾空格
        print(line.strip())


def test_read_line_by_line():
    print("准备读文件")
    # 用异常捕捉的方式 检查文件是否存在
    try:
        file = open(file_name, 'r', encoding='utf-8')
        line = file.readline()
        # 空字符串 "" 被视为 False，有内容的字符串被视为 True
        while line:
            print(line.strip())
            line = file.readline()
    except FileNotFoundError:
        # 如果文件不存在，捕获异常并提示
        print(f"错误：文件 '{file_name}' 不存在。")


def test_read2():
    print("准备读文件")
    # f = open("foo.txt", "r")
    try:
        file = open(file_name, 'r', encoding='utf-8')
        # read[(size)]方法 文件读取指定的字节数，如果未给定或为负则读取所有。
        content = file.read()  # 读取整个文件内容
        print(content)  # 打印内容
    except FileNotFoundError:
        # 如果文件不存在，捕获异常并提示
        print(f"错误：文件 '{file_name}' 不存在。")


#


if __name__ == '__main__':
    # test_input()
    # test_write()
    # os.remove(file_name) #删除文件. 文件不存在 会报错
    test_read_all_content()
