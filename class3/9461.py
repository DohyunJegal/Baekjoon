import sys
input = sys.stdin.readline

lst = [0]*101
tmp = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for i in range(101):
    if i < 11:
        lst[i] = tmp[i]
    else:
        lst[i] = lst[i-1] + lst[i-5]

n = int(input())
for _ in range(n):
    print(lst[int(input())])
