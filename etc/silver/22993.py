import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
j = lst.pop(0)
lst.sort()

for i in lst:
    if j > i:
        j += i
    else:
        print('No')
        exit()
print('Yes')