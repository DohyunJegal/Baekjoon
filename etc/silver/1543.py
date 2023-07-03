import sys
input = sys.stdin.readline

orig = input().rstrip()
find = input().rstrip()

curr = 0
res = 0
while curr < len(orig):
    if orig[curr:curr+len(find)] == find:
        curr += len(find)
        res += 1
    else:
        curr += 1

print(res)
