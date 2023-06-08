import sys
input = sys.stdin.readline

n = int(input())
files = []
for _ in range(n):
    files.append(list(input().rstrip()))
res = files[0]

for i in range(n):
    for j in range(len(res)):
        if files[i][j] != res[j]:
            res[j] = '?'

for k in res:
    print(k, end='')
