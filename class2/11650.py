import sys
input = sys.stdin.readline

n = int(input())
lst = [[0, 0] for _ in range(n)]

for i in range(n):
    a, b = map(int, input().split())
    lst[i] = [a, b]

lst.sort()

for j in range(n):
    print(lst[j][0], lst[j][1])