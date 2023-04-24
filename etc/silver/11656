import sys
from collections import deque

input = sys.stdin.readline

s = deque(input().rstrip())
lst = []

while s:
    tmp = ''
    for i in s:
        tmp += i
    lst.append(tmp)
    s.popleft()

for j in sorted(lst):
    print(j)
