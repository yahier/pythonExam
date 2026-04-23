# 异常捕捉

###todo 标准例子
def test1():
    fh = open("testfile2", "w")
    try:
        fh.write("这是一个测试文件，用于测试异常!!")
        # fh.read()
        test_raise_except(2)
        print("try的最后语句")
    except (IOError, ValueError) as e:
        print("Error: 没有找到文件或读取文件失败")
        print(f"异常信息: {e}")
    except  ZeroDivisionError:
        print("除零错误")
    else:  # point 如果 try语句块成功执行（没有异常），才会继续执行这里的else语句块
        print("内容写入文件成功")
        fh.close()
    finally:
        print("关闭文件")
        fh.close()


# point 这里的: int表示期待入参是一个int类型
def test_raise_except(level: int):
    if level < 1:
        raise Exception("Invalid level!", level)
        # 触发异常后，后面的代码就不会再执行


if __name__ == '__main__':
    test1()
