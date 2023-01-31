lst = list(map(int, input().split()))

s = 0
for i in lst:
    s += i * i

print(s % 10)