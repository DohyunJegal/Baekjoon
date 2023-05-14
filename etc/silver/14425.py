import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
s = deque([])
for _ in range(n):
    s.append(str(input().rstrip()))
cnt = 0
for _ in range(m):
    if str(input().rstrip()) in s:
        cnt += 1

print(cnt)