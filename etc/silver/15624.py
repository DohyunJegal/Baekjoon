import sys
input = sys.stdin.readline

n = int(input())
lst = [0]*1000001
lst[0], lst[1] = 0, 1
for i in range(2, n+1):
    lst[i] = (lst[i-1]+lst[i-2])%1000000007
print(lst[n])
