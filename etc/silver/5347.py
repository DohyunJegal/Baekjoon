import sys
input = sys.stdin.readline

def gcd(x, y):
    while y>0:
        x, y = y, x%y
    return x

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(int(a*b/gcd(a, b)))
