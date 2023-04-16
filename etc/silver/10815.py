import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
card = list(sorted(map(int, input().split())))
m = int(input())
geun = list(map(int, input().split()))

def search(array, check, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == check:
            return 1
        elif array[mid] > check:
            end = mid - 1
        else:
            start = mid + 1
    return 0

for i in geun:
    print(search(card, i, 0, n-1), end=' ')