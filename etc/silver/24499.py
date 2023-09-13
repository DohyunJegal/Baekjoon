import sys
from itertools import accumulate
input = sys.stdin.readline

n, k = map(int, input().split())
pie = list(map(int, input().split()))
piesum = [0]+list(accumulate(pie))

piemax = 0
for i in range(n):
    if i+k <= n:
        piemax = max(piemax, piesum[i+k]-piesum[i])
    else:
        piemax = max(piemax, piesum[n]-piesum[i]+piesum[(i+k)%n])
print(piemax)