import sys
input = sys.stdin.readline

x = int(input())
i = 0
while x > i:
    x -= i
    i += 1

if i%2==0:
    print(x, (i+1)-x, sep='/')
else:
    print((i+1)-x, x, sep='/')