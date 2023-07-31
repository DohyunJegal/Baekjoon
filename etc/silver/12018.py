import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = []
for _ in range(n):
    p, l = map(int, input().split())
    q = sorted(list(map(int, input().split())), reverse=True)
    if len(q) < l:
        lst.append(1)
    else:
        lst.append(q[l-1])
lst.sort()

cnt = 0
for i in lst:
    if i <= m:
        cnt += 1
        m -= i

print(cnt)
