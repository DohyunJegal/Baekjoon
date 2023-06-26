import sys
input = sys.stdin.readline

n, c = map(int, input().split())
msg = list(map(int, input().split()))
lst = {}
for i in msg:
    if i in lst:
        lst[i] += 1
    else:
        lst[i] = 1
lst = dict(sorted(lst.items(), key=lambda x:-x[1]))
for j in lst:
    for k in range(lst[j]):
        print(j, end=' ')
