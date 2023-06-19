import sys
input = sys.stdin.readline

a, b = map(int, input().split())
res = abs(a-b)
for _ in range(int(input())):
    m = int(input())
    if res > abs(m-b):
        res = abs(m-b) + 1
print(res)
