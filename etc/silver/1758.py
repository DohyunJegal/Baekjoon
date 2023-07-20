import sys
input = sys.stdin.readline

lst = []
for _ in range(int(input())):
    lst.append(int(input()))
lst.sort(reverse=True)

res = 0
for i in range(len(lst)):
    if lst[i]-i > 0:
        res += lst[i] - i
print(res)
