import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lstA = list(map(int, input().split()))
lstB = list(map(int, input().split()))
for i in sorted(lstA + lstB):
    print(i, end=' ')