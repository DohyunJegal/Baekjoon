import sys
input = sys.stdin.readline().rstrip

str = input().split('-')
lst = []

for i in str:
    tmp = i.split('+')
    s = 0
    for j in tmp:
        s += int(j)
    lst.append(s)

res = lst[0]
for k in range(1, len(lst)):
    res -= lst[k]
print(res)