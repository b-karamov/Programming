import sys
import argparse

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-N', '--Number')
    parser.add_argument('-a', '--all', nargs='?', default=False, const=True)
    parser.add_argument('-f', '--filepath', nargs='?', default=sys.stdout, type = argparse.FileType('w'))
    return parser

parser = createParser()
namespace = parser.parse_args()
N = int(namespace.Number)

def fib(N):
    if N == 2 or N == 1:
        return 1
    return fib(N-1) + fib(N-2)

# сейчас будет медленный код, но мне лень его оптимизировать
res = []
for i in range(1, N+1):
    res.append(fib(i))
print(res)
if namespace.all != False:
    namespace.filepath.write(' '.join(list(map(lambda x: str(x), res))))
else:
    namespace.filepath.write(str(res[-1]))
