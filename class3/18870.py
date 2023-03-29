import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
ord_lst = sorted(set(lst))
res = {}
cnt = 0

for i in ord_lst:
    res[i] = cnt
    cnt += 1

for j in lst:
    print(res.get(j), end=' ')