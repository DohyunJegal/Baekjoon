import sys
input = sys.stdin.readline

n = int(input())
lst = []

for _ in range(n):
    r = int(input())
    if r == 0 and len(lst) != 0:
        del lst[-1]
    else:
        lst.append(r)

print(sum(lst))