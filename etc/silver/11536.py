import sys
input = sys.stdin.readline

lst = []
for _ in range(int(input())):
	lst.append(input().rstrip())
if lst == sorted(lst):
	print('INCREASING')
elif lst == sorted(lst, reverse=True):
	print('DECREASING')
else:
	print('NEITHER')
