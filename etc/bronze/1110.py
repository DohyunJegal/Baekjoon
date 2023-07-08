import sys
input = sys.stdin.readline

n = int(input())
tmp = n
cnt = 0

while True:
	l = tmp%10
	r = ((tmp//10)+l)%10
	tmp = (l*10)+r
	cnt += 1
	
	if tmp == n:
		break
		
print(cnt)
