# 异常捕捉

###todo 标准例子
def test1():
    fh = open("testfile2", "w")
    try:
        # fh.write("这是一个测试文件，用于测试异常!!")
        fh.read()
        print("try的最后语句")
    except (IOError, ValueError) as e:
        print("Error: 没有找到文件或读取文件失败")
        print(f"异常信息: {e}")
    except  ZeroDivisionError:
        print("除零错误")
    else:
        print("内容写入文件成功")
        fh.close()
    finally:
        print("关闭文件")
        fh.close()


def test_raise_except(level):
    if level < 1:
        raise Exception("Invalid level!", level)
        # 触发异常后，后面的代码就不会再执行


if __name__ == '__main__':
    test1()
