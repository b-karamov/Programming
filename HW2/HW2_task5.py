try:
    for i in [-1, 0, 1]:
        print('Сейчас будем делить на', i)
        print(1/i)
except ZeroDivisionError:
    print('Ты делишь на ноль!')
else:
    print('Ошибка не произошла')
finally:
    print('А я в любом случае печатаюсь')
