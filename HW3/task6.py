import sys
import argparse
import time

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-N', '--Number')
    parser.add_argument('-f', '--filepath')
    return parser

def file_with_logs(func):
    def wrapper(n, file):
        start = time.time()
        fact = func(n)
        end = time.time()
        with open(file, 'w') as file:
            file.write(f'Время вызова функции: {start}\nВходящие аргументы: {n}\nВозвращает: {fact}\nВрем завершения работы: {end}\nВремя работы: {end-start}')
    return wrapper

@file_with_logs
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

parser = createParser()
namespace = parser.parse_args()
N = int(namespace.Number)
file = namespace.filepath

factorial(N, file)


