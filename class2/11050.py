import sys
input = sys.stdin.readline

n, m = map(int, input().split())
np = kp = nkp = 1
# np = n!, kp = k!, nkp = (n-k)!
for i in range(1, n+1):
    np *= i
for j in range(1, m+1):
    kp *= j
for k in range(1, n-m+1):
    nkp *= k

if 0 <= m <= n:
    print(int(np/(kp*nkp)))
else:
    print('0')