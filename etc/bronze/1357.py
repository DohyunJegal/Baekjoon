import sys
input = sys.stdin.readline

def rev(n):
    return int(str(n)[::-1])

x, y = map(int, input().split())
print(rev(rev(x)+rev(y)))