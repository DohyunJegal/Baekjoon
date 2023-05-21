import sys
input = sys.stdin.readline

lst = []
n = int(input())
for _ in range(n):
    lst.append(int(input()))
lst.reverse()

cnt = 0
for i in range(1, n):
    if lst[i-1] <= lst[i]:
        cnt += lst[i] - lst[i-1] + 1
        lst[i] = lst[i-1] - 1

print(cnt)