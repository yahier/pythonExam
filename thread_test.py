# point 线程相关
import threading
import time
from concurrent.futures import ThreadPoolExecutor


def test_thread(name):
    print(f"{name} 开始咯")
    time.sleep(5)
    print(f"{name} end")


def start1():
    try:
        t1 = threading.Thread(target=test_thread, args=("A",))
        t1.start()
    except Exception as e:
        print(e)
    finally:
        print("finally")


# point 用线程池启动线程
def start2():
    with ThreadPoolExecutor(max_workers=3) as executor:
        # 提交任务
        futures = [executor.submit(test_thread, i) for i in range(3)]
        # 获取结果
        for future in futures:
            print(future.result())


def test_loop():
    # point  生成 [0, 2] (range(3) 里的偶数)
    evens = [i for i in range(3) if i % 2 == 0]

    # mark 列表推导式
    list1 = [i for i in range(3)]
    for i in list1:
        print(i)


if __name__ == '__main__':
    # start2()
    test_loop()
