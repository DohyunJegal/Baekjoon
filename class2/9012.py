import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    lst = list(input().rstrip())
    cnt = 0
    for i in lst:
        if i == '(':
            cnt += 1
        elif i == ')':
            cnt -= 1

        if cnt < 0:
            break
    print('YES' if cnt == 0 else 'NO')