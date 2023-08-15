import sys
input = sys.stdin.readline

p, n = map(int, input().split())
lst = sorted(list(map(int, input().split())))

cnt = 0
for i in lst:
    if p >= 200:
        break
    cnt += 1
    p += i
print(cnt)