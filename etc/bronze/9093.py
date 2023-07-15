import sys
input = sys.stdin.readline

for _ in range(int(input())):	 
	for i in list(input().rstrip().split()): 
		print(i[::-1], end=' ')
