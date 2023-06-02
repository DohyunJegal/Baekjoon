import sys
input = sys.stdin.readline

n = int(input())
lst = sorted(list(map(int, input().split())))
print(lst[(n-1)//2])
