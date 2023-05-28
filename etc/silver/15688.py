import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
	lst.append(int(input()))
for i in sorted(lst):
	print(i)
