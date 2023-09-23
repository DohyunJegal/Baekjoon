import sys
input = sys.stdin.readline

cnt = 0
while True:
    n = int(input())
    if n == 0:
        break
    else:
        cnt += 1
        lst = sorted(list(input().rstrip() for _ in range(n)))
        print(cnt)
        for i in lst:
            print(i)