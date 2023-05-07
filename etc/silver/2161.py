import sys
from collections import deque

input = sys.stdin.readline

lst = deque([])
res = []
n = int(input())
for i in range(1, n+1):
  lst.append(i)
while lst:
  if lst:
    res.append(lst.popleft())
  if lst:
    lst.append(lst.popleft())

for j in res:
  print(j, end=' ')
