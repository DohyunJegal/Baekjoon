import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
for i in sorted(lst):
	print(i, end=' ')
