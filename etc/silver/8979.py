import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))
lst.sort(key=lambda x:(x[1],x[2],x[3]), reverse=True)

index = 0
for i in range(n):
    if lst[i][0] == k:
        index = i
        break
for j in range(n):
    if lst[j][1:] == lst[index][1:]:
        print(j+1)
        break