import sys
from collections import deque
input = sys.stdin.readline

lst = deque([])
for _ in range(int(input())):
    a = input().split()
    if int(a[0]) == 1:
        lst.appendleft(int(a[1]))
    elif int(a[0]) == 2:
        lst.append(int(a[1]))
    elif int(a[0]) == 3:
        print(lst.popleft() if lst else -1)
    elif int(a[0]) == 4:
        print(lst.pop() if lst else -1)
    elif int(a[0]) == 5:
        print(len(lst))
    elif int(a[0]) == 6:
        print(0 if lst else 1)
    elif int(a[0]) == 7:
        print(lst[0] if lst else -1)
    elif int(a[0]) == 8:
        print(lst[-1] if lst else -1)