import numpy as np
import pandas as pd


def test_1():
    scores = np.random.randint(50, 101, (5, 3))
    names = ('关羽', '张飞', '赵云', '马超', '黄忠')
    courses = ('语文', '数学', '英语')
    df = pd.DataFrame(data=scores, columns=courses, index=names)

    print(df)
    print("\n计算每门课程成绩的平均分\n", df.mean())
    # mark mean方法的axis参数，默认为0，计算每列。1时计算每行
    print("\n每个人的平均分\n", df.mean(axis=1))


if __name__ == '__main__':
    test_1()
