import sys
input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    lst = {}
    res = 0
    for _ in range(n):
        lst[int(input())] = 1
    for _ in range(m):
        if int(input()) in lst:
            res += 1

    print(res)
