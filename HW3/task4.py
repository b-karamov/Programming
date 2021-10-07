def decorator(func):
    def wrapper(arr):
        n = func(arr)
        if n == 0:
            print('Нет\(')
        elif n > 10:
            print('Очень много')
        else:
            print(n)
    return wrapper

@decorator
def number_of_even(arr):
    n = 0
    for number in arr:
        if number % 2 == 0:
            n += 1
    return n

arr = []
a = input('Введи число. Чтобы закончить, введи #: ')
while a != '#':
    arr.append(int(a))
    a = input('Введи число: ')

number_of_even(arr)
