import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
q = deque([])
for _ in range(n):
    o = input().split()
    
    if o[0] == "push":
        q.append(o[1])
    elif o[0] == "pop":
        print(q.popleft() if q else -1)
    elif o[0] == "size":
        print(len(q))
    elif o[0] == "empty":
        print(0 if q else 1)
    elif o[0] == "front":
        print(q[0] if q else -1)
    elif o[0] == "back":
        print(q[-1] if q else -1)
