import sys

input = sys.stdin.readline

n = int(input())
lst = []
check = count = 0
for _ in range(n):
    s, e = map(int, input().split())
    lst.append([s, e])
lst.sort(key=lambda x: x[0])
lst.sort(key=lambda x: x[1])

for i in lst:
    if i[0] >= check:
        check = i[1]
        count += 1

print(count)