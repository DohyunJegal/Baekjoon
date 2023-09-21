import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
prop = [list(map(int, input().split())) for _ in range(n)]

res = 0
for a, b, c in combinations(range(m), 3):
    tmp = 0
    for i in range(n):
        tmp += max(prop[i][a], prop[i][b], prop[i][c])
    res = max(res, tmp)

print(res)