import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(int(input()))
lst.sort(reverse=True)
cnt = 0

for i in lst:
    cnt += k // i
    k %= i
print(cnt)