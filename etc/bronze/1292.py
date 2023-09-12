import sys
input = sys.stdin.readline

a, b = map(int, input().split())
lst = []

i = 1
while len(lst) < b:
    for _ in range(i):
        lst.append(i)
    i += 1
print(sum(lst[a-1:b]))