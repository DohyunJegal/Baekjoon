import sys
input = sys.stdin.readline

e, s, m = map(int, input().split())
a, b, c, res = 1, 1, 1, 1

while True:
    if e == a and s == b and c == m:
        print(res)
        break
    a += 1
    if a > 15:
        a = 1
    b += 1
    if b > 28:
        b = 1
    c += 1
    if c > 19:
        c = 1
    res += 1