# @author: SFQRM
# first edit time: 2019-10-14
# function：
#     super() usage
#     super()函数是用于调用父类的一个方法。
#     super()语法：super(type[, object-or-type])
#                       type -- 类。
#                       object-or-type -- 类，一般是self


# """
#   Python3.x 实例
#   Python3.x 和 Python2.x 的一个区别是: Python 3 可以使用直接使用 super().xxx 代替 super(Class, self).xxx
# """
class A():
    def add(self, x):
        y = x+1
        print(y)


class B(A):
    def add(self, x):
        super().add(x)


# b = B()
# b.add(2)


class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        print('Parent')

    def bar(self, message):
        print("%s from Parent" % message)


class FooChild(FooParent):
    def __init__(self):
        # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类 FooChild 的对象转换为类 FooParent 的对象
        # super(FooChild, self).__init__()
        super().__init__()
        print('Child')

    def bar(self, message):
        # super(FooChild, self).bar(message)
        super().bar(message)
        print('Child bar fuction')
        print(self.parent)


if __name__ == '__main__':
    fooChild = FooChild()
    fooChild.bar('HelloWorld')
    
    
# Output:
#     Parent
#     Child
#     HelloWorld from Parent
#     Child bar fuction
#     I'm the parent.
