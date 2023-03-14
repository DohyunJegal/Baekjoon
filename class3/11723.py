import sys

input = sys.stdin.readline

m = int(input())
lst = set()
for _ in range(m):
    tmp = input().split()
    order = tmp[0]
    if len(tmp) == 2:
        num = int(tmp[1])

    if order == 'add':
        lst.add(num)
    elif order == 'remove':
        lst.discard(num)
    elif order == 'check':
        print(1 if num in lst else 0)
    elif order == 'toggle':
        if num in lst:
            lst.discard(num)
        else:
            lst.add(num)
    elif order == 'all':
        lst = set([i for i in range(1, 21)])
    elif order == 'empty':
        lst = set()