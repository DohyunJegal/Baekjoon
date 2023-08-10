import sys
input = sys.stdin. readline

n = int(input())
min, max = 1, n

while min <= max:
    mid = (min+max)//2
    if mid**2 == n:
        print(mid)
        break
    elif mid**2 > n:
        max = mid
    else:
        min = mid

# import math
# print(math.isqrt(int(input())))