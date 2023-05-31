import sys
input = sys.stdin.readline

lst = [0, 1]
n = int(input())

for i in range(1, n):
	lst.append(lst[i]+lst[i-1])
	
print(lst[n])
