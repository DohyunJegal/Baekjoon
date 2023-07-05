import sys
input = sys.stdin.readline

n, l = map(int, input().split())
h = sorted(list(map(int, input().split())))

for i in h:
    if i <= l:
        l += 1
    else:
        break
print(l)
