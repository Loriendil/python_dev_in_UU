# Домашнее задание по теме "Интроспекция"
from pprint import pprint
import inspect # Это возьмём из лекции "Лекция. Интроспекция. 1.2"

class MyClass:
    def __init__(self):
        self.attr_01 = 27
        self.attr_02 = 'string'

    def Fibonacci(self, n):
        if n < 0:
            return 0

        elif n == 0:
            return 0

        elif n == 1:
            return 1
        else:
            return self.Fibonacci(n - 1) + self.Fibonacci(n - 2)

    def method2(self):
        print("this is method2")

class A(MyClass):
    pass

def introspection_info(obj):
    _list = dir(obj)

    result = {'тип объекта': type(obj),
              'атрибуты объекта': [attr for attr in _list if not callable(getattr(obj, attr))],
              'методы объекта': [method for method in _list if callable(getattr(obj, method))],
              'принадлежность к модулю': obj.__module__ if hasattr(obj, '__module__')  else type(obj)}

    return result

def shorted_introspection_info(obj):
    _list = dir(obj)
    result = {'тип объекта': type(obj),
              'атрибуты объекта': [name for name, value in inspect.getmembers(obj) if not callable(value) and not name.startswith("__")],
              'методы объекта': [method for method in _list if callable(getattr(obj, method))],
              'принадлежность к модулю': inspect.getmodule(obj),
              'сигнатура метода': inspect.signature(obj.__init__),
              'Является ли модулем': inspect.ismodule(obj),
              'Получаем строку документации': inspect.getdoc(obj)
              }

    return result


mcl = MyClass()
mcl.Fibonacci(12)
aa = A()

number_info = introspection_info(42)
custom_info = introspection_info(mcl)
pprint(number_info)
pprint(custom_info)

print('----------------------------------------------------------------------------------------------')

num_info = shorted_introspection_info(55)
cus_info = shorted_introspection_info(aa)
pprint(num_info)
pprint(cus_info)


