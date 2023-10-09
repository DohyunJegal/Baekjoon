s, m = 0, 0
for _ in range(4):
    o, i = map(int, input().split())
    s += (i-o)
    m = max(m, s)
print(m)