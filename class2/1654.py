import sys
from collections import deque
input = sys.stdin.readline

k, n = map(int, input().split())
lst = []
for _ in range(k):
    lst.append(int(input()))

maxLen = max(lst)
minLen = 1
while minLen <= maxLen:
    mid = (minLen+maxLen)//2
    sum = 0
    for i in lst:
        if i // mid > 0:
            sum += i // mid
    if sum >= n:
        minLen = mid + 1
    else:
        maxLen = mid - 1

print(maxLen)