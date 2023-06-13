import sys
input = sys.stdin.readline

k, l = map(int, input().split())
lst = {}
for i in range(l):
    lst[input().rstrip()] = i
lst = sorted(lst.items(), key=lambda x:x[1])

if k > len(lst):
    k = len(lst)
for j in range(k):
    print(lst[j][0])
