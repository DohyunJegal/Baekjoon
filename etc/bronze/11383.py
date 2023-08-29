import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [input().rstrip() for _ in range(n)]
b = [input().rstrip() for _ in range(n)]

for i in range(n):
    tmp = ''
    for j in a[i]:
        tmp += j*2
    if tmp != b[i]:
        print('Not Eyfa')
        exit()
print('Eyfa')