# @Author: SFQRM
# First edit time: 2019.10.14
# Function:
#     python usage


# 定义类
class Student(object):                                              # object类是所有类都会继承的类
    """
        __init__(self, name1, name2, ...): 内置方法将必须绑定给实例的属性写入
        方法的第一参数永远是self，表示创建的类实例本身。
        在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
    """
    def __init__(self, name, score):
        # self.name = name
        # self.score = score
        self.__name = name                                          # 在Python中，实例的变量名如果以'__'开头，就变成了私有变量（private）
        self.__score = score                                        # 只有内部可以访问，外部不能访问

    def print_score(self):
        print("%s:%s" % (self.__name, self.__score))                # 格式化输出

    def get_name(self):                                             # 外部代码可以获取name
        return self.__name

    def get_score(self):                                            # 外部代码可以获取score
        return self.__score


# 定义实例
student = Student("Chuck", 99)
# print(student.__name)                                               # 因为‘__name’是内部私有变量
'''
    因为‘__name’是内部私有变量，
    所以无法从外部访问实例变量.__name和实例变量.__score
    Output:
    Traceback (most recent call last):
        File "D:/code/Python/workplace/MXNet/Demo.py", line 26, in <module>
            print(student.__name)                                               # 因为‘__name’是内部私有变量，
    AttributeError: 'Student' object has no attribute '__name'
'''
# student.print_score()


class Test:
    def ppr(self):
        print(self)
        print(self.__class__)


t = Test()
t.ppr()
