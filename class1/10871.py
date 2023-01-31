a, b = map(int, input().split())
lst = list(map(int, input().split()))
tmp = []
for i in lst:
    if i < b:
        tmp.append(i)
print(*tmp)