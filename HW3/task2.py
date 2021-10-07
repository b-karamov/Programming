import sys
import argparse

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-N', '--Number')

    return parser

parser = createParser()
namespace = parser.parse_args()
N = int(namespace.Number)

def fib(N):
    if N == 2 or N == 1:
        return 1
    return fib(N-1) + fib(N-2)

print(f'{N}-е число Фибоначчи: {fib(N)}')

