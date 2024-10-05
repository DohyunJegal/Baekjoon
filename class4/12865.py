import sys
input = sys.stdin.readline

items, weight = map(int, input().split())
item_list = [[0, 0]]
for _ in range(items):
    item_list.append(list(map(int, input().split())))
d = [[0]*(weight+1) for _ in range(items+1)]

for i in range(1, items+1):
    for j in range(1, weight+1):
        w, v = item_list[i][0], item_list[i][1]
        if j >= item_list[i][0]:
            d[i][j] = max(d[i-1][j], d[i-1][j-w]+v)
        else:
            d[i][j] = d[i-1][j]
print(d[items][weight])