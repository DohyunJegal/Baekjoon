import sys
input = sys.stdin.readline

n = int(input())
tmp = cnt = res = 0

while cnt < n:
    if '666' in str(tmp):
        res = tmp
        cnt += 1
    tmp += 1

print(res)