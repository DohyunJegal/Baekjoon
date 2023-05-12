import sys
input = sys.stdin.readline

lst = []
res = []
n, k = map(int, input().split())
for i in range(2, n+1):
    lst.append(i)
while lst:
    tmp = lst[0]
    for j in lst:
        if j%tmp == 0:
            res.append(j)
            lst.remove(j)
print(res[k-1])