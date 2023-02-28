import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
d = [0] * (n+1)

for i in range(1, n+1):
    d[i] = d[i-1] + min(lst)
    lst.remove(min(lst))
print(sum(d))