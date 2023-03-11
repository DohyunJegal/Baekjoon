import sys
input = sys.stdin.readline

n, m = map(int, input().split())
setD = set(input().rstrip() for _ in range(n))
setB = set(input().rstrip() for _ in range(m))
listDB = sorted(list(setD & setB))

print(len(listDB))
for i in listDB:
    print(i)