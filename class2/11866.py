import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = list(i for i in range(1, n+1))
p = k-1

print('<', end='')
while lst:
    if p >= len(lst):
        p %= len(lst)
    if len(lst) > 1:
        print(lst.pop(p), end=', ')
    else:
        print(lst.pop(p), end='')
    p += k-1
print('>')