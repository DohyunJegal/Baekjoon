import sys
input = sys.stdin.readline

n = int(input())
lst = {}
for _ in range(n):
    tmp = input().rstrip()
    if tmp in lst:
        lst[tmp] += 1
    else:
        lst[tmp] = 1
for _ in range(n-1):
    tmp = input().rstrip()
    lst[tmp] -= 1
for i in lst:
    if lst[i]:
        print(i)
        break
