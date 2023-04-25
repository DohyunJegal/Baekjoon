import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
lst = deque([i for i in range(1, n+1)])
res = []

while lst:
    for i in range(k-1):
        lst.append(lst.popleft())
    res.append(str(lst.popleft()))

print('<', ', '.join(res), '>', sep='')
