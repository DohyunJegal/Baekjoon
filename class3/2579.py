import sys
input = sys.stdin.readline

n = int(input())
lst = [0]*301
d = [0]*301
for i in range(n):
    lst[i] = int(input())

d[0] = lst[0]
d[1] = lst[0] + lst[1]
# 1칸 2번 or 2칸
d[2] = max(lst[1]+lst[2], lst[0]+lst[2])
for j in range(3, n):
    # 2칸 후 1칸 or 2칸
    d[j] = max(d[j - 3] + lst[j - 1] + lst[j], d[j - 2] + lst[j])
print(d[n-1])