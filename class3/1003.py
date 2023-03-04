import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())

    d0 = deque([1, 0])
    d1 = deque([0, 1])
    for i in range(2, n+1):
        d0.append(d0[i-1] + d0[i-2])
        d1.append(d1[i-1] + d1[i-2])

    if n == 0:
        print(d0[0], d1[0])
    else:
        print(d0[-1], d1[-1])