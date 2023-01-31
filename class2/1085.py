lst = list(map(int, input().split()))
x = lst[0] if lst[0] < lst[2] - lst[0] else lst[2] - lst[0]
y = lst[1] if lst[1] < lst[3] - lst[1] else lst[3] - lst[1]
print(x if x < y else y)