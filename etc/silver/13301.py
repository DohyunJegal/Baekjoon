import sys
input = sys.stdin.readline

lst = [0]*81
lst[1], lst[2] = 4, 6
n = int(input())
for i in range(3, n+1):
	lst[i] = lst[i-1] + lst[i-2]
print(lst[n])
