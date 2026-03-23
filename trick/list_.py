import math
from random import randrange
import class_1


# 将一颗色子掷6000次，统计每种点数出现的次数
def test_statistics():
    counters = [0] * 6  # point 创建一个包含 6 个元素的列表，每个元素的初始值都是 0
    for i in range(600):
        i = randrange(1, 7)  # point 左闭右开原则，得到的随机数范围包含1，不包含7
        counters[i - 1] += 1
    for i in range(0, 6):
        print(f"{i + 1}出现的次数是 {counters[i]}")


# point 列表排序
def sort_list():
    dog = class_1.Animal("dog", 3)
    cat = class_1.Animal("cat", 2)
    ant = class_1.Animal("ant", 0.1)
    bird = class_1.Animal("bird", 0.5)
    animals = [dog, cat, ant, bird]
    # mark 按年龄从小到大排序，便捷语法
    animals.sort(key=lambda x: x.age)
    # mark 按年龄从小到大排序, 使用类方法,这也是最广泛的方法
    animals.sort(key=class_1.Animal.get_age2)
    # mark 按年龄从大到小排序
    animals.sort(key=lambda x: x.age, reverse=True)
    for animal in animals:
        print(animal.name, animal.age)


if __name__ == '__main__':
    # test_statistics()
    sort_list()
