import sys
input = sys.stdin.readline

l = int(input())
st = list(input().rstrip())

for i in range(l):
   st[i] = (ord(st[i])-96)*(31**i)

print(sum(st)%1234567891)