import sys
input = sys.stdin.readline

n = int(input())
t = [1]*36
for i in range(1, n+1):
    tmp = 0
    for j in range(i):
        tmp += t[j]*t[i-j-1]
    t[i] = tmp
print(t[n])
