print('Не будем изобретать велосипед, сделаем просто')
arr = []
a = input('Введи число. Чтобы закончить, введи #: ')
while a != '#':
    arr.append(int(a))
    a = input('Введи число: ')

def swap(func):
    def wrapper(arr):
        arr = arr[::-1]
        func(arr)
    return wrapper

@swap
def print_list(arr):
   print('Ты ввел числа', *arr)

print_list(arr)
