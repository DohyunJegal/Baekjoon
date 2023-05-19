import sys
input = sys.stdin.readline

n, d = map(int, input().split())
lst = {}
for i in range(1, n+1):
	for j in str(i):
		if j not in lst:
			lst[j] = 1
		else:
			lst[j] += 1
print(lst[str(d)])