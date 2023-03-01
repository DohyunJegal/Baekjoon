import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(int(input()))
lst.sort()
cnt = 0

while k != 0:
    mx = lst[0]
    for i in lst:
        if mx < i <= k:
            mx = i
    cnt += k // mx
    k %= mx
print(cnt)