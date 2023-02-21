import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    arr = deque(map(int, input().split()))
    count = 0

    while arr:
        b -= 1
        if arr[0] != max(arr):
            arr.append(arr.popleft())
            if b < 0:
                b = len(arr)-1
        else:
            count += 1
            arr.popleft()
            if b < 0:
                print(count)
                break