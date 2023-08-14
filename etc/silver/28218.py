import sys
from collections import deque
input = sys.stdin.readline

lst = deque([])
for _ in range(int(input())):
    order = list(map(int, input().split()))
    if order[0] == 1:
        lst.append(order[1])
    elif order[0] == 2:
        print(lst.pop() if lst else -1)
    elif order[0] == 3:
        print(len(lst))
    elif order[0] == 4:
        print(0 if lst else 1)
    elif order[0] == 5:
        print(lst[-1] if lst else -1)