import sys
from collections import deque

input = sys.stdin.readline

def d(n):
    tmp = list(map(int, str(n)))
    return n + sum(tmp)

lst = deque([i for i in range(10001)])
for j in range(10001):
    tmp = d(j)
    if tmp in lst:
        lst.remove(tmp)

for k in lst:
    print(k)