class Animal:
    # point 类变量 它的值将在这个类的所有实例之间共享。你可以在内部类或外部类使用 Animal.animal_count 访问
    # point 类似于JAVA中的静态变量
    animal_count = 0
    _secret_food = 0  # mark 前面增加了_后，变为类的protect变量
    __secretCount = 0  # mark 前面增加了__后，变为类的private变量

    # mark _init__()方法是构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Animal.animal_count = Animal.animal_count + 1

    # mark 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是self
    # point 增加注解 @property 后，方法变成“只读属性”，调用时不用加()
    @property
    def speak(self):
        print(f"动物叫了一声 我是{self.name} 动物总数{Animal.animal_count}")
        # del self.name #mark 删除这个实例的name属性，但一般也不需要删除啊

    def get_age2(animal):
        return animal.age

    @staticmethod
    def go_():
        print("我是类的静态方法，我可以动起来")


def test1():
    cat = Animal("cat", 1)
    cat.weight = 4  # mark 动态添加属性
    cat.speak
    print("我是cat，我的体重kg数是 ", cat.weight)


class Movable:
    def move(self):
        print("我可以移动")


# point 类继承；注意这里的多继承
class Dog(Animal, Movable):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print(f"狗叫了一声 我是{self.name} 狗的颜色是{self.color}")

    def move(self):
        print("我可以跑的很快")


# point 这个函数不关心传入的对象是 Dog 还是 Cat,它只要求对象必须有 speak()方法
def make_animal_speak(animal):
    print(animal.speak())
    print(animal.eat())  # mark 瞎写方法也不会报错，只会在运行时检查


def test2():
    cat = Animal("cat", 1)
    dog = Dog("大黄", 2, "黄色")
    dog.speak()
    dog.move()

    Animal.go_()


if __name__ == "__main__":
    test1()
    #test2()
