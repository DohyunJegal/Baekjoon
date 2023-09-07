import sys
input = sys.stdin.readline

d = [0, 5]
delta = 7

n = int(input())
for i in range(n+1):
	d.append((d[-1]+(delta+(i*3)))%45678)
print(d[n])
