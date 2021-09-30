def f1():
    f2()
def f2():
    f3()
def f3():
    raise MyException('Что-то не так')
class MyException(Exception):
    pass

f1()
