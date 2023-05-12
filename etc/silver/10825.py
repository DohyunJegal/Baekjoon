import sys
input = sys.stdin.readline

lst = []
n = int(input())
for _ in range(n):
    name, k, e, m = input().split()
    lst.append((name, int(k), int(e), int(m)))
lst.sort(key=lambda x:x[0])
lst.sort(key=lambda x:-x[3])
lst.sort(key=lambda x:x[2])
lst.sort(key=lambda x:-x[1])

for i in lst:
    print(i[0])
