import sys
input = sys.stdin.readline

n = int(input())
lst = sorted(list(set(map(int, input().split()))))
for i in lst:
    print(i, end=' ')