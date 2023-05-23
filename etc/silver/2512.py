import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
m = int(input())

low, high = 1, max(lst)
while low <= high:
    tmp = 0
    mid = (low+high)//2
    for i in lst:
        if i <= mid:
            tmp += i
        else:
            tmp += mid
    if tmp <= m:
        low = mid+1
    else:
        high = mid-1
print(high)