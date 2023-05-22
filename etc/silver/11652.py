import sys
input = sys.stdin.readline

lst = []
cnt = {}
n = int(input())
for _ in range(n):
    lst.append(int(input()))
lst.sort()
for i in lst:
    if i not in cnt:
        cnt[i] = 1
    else:
        cnt[i] += 1
print(max(cnt, key=cnt.get))