import sys
input = sys.stdin.readline

lst = list(map(int, input().rstrip()))
tmp = 0
for i in lst:
	tmp += i
cnt = 0
if tmp >= 10:
	cnt = 1
	while tmp >= 10:
		lst = list(map(int, str(tmp)))
		tmp = 0
		for j in lst:
			tmp += j
		cnt += 1
	
print(cnt)
print("YES" if tmp%3==0 else "NO")
