import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
lst = deque([])
res = deque([])
num = 1
flag = 0

for _ in range(n):
    tmp = int(input())

    while num <= tmp:
        lst.append(num)
        res.append('+')
        num += 1

    if lst[-1] == tmp:
        lst.pop()
        res.append('-')
    else:
        print('NO')
        flag = 1
        break

if flag != 1:
    for i in res:
        print(i)