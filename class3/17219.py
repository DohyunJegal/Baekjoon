import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pwList = {}

for _ in range(n):
    link, pw = input().split()
    pwList[link] = pw

for _ in range(m):
    site = input().rstrip()
    print(pwList[site])