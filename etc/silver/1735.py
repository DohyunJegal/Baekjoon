import sys
input = sys.stdin.readline

# 최대공약수, 유클리드 호제법
def GCD(a, b):
    m = a % b
    while m > 0:
        a = b
        b = m
        m = a % b
    return b

a, b = map(int, input().split())
c, d = map(int, input().split())
n = GCD(a*d+c*b, b*d)
print((a*d+c*b)//n, (b*d)//n)