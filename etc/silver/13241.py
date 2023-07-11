import sys
input = sys.stdin.readline
	
def gcd(x, y):	# 최대공약수
    while y>0:
        x, y = y, x%y
    return x

a, b = map(int, input().split())
print(int(a*b/gcd(a, b)))	# 최소공배수
