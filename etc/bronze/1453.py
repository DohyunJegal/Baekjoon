import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
pc = {}
reject = 0

for i in lst:
	if i not in pc:
		pc[i] = 1
	else:
		reject += 1
		
print(reject)
