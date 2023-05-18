import sys
from collections import deque
input = sys.stdin.readline

queue = deque(input().rstrip())
cnt = 0
i = 0

while queue:
    i = 0
    
    if len(queue) > 1:
        if queue[0] == 'c':
            if queue[1] == '=' or queue[1] == '-':
                i = 2
            else:
                i = 1
        elif queue[0] == 'd':
            if len(queue) > 2 and queue[1] == 'z' and queue[2] == '=':
                i = 3
            elif queue[1] == '-':
                i = 2
            else:
                i = 1
        elif queue[0] == 'l':
            if queue[1] == 'j':
                i = 2
            else:
                i = 1
        elif queue[0] == 'n':
            if queue[1] == 'j':
                i = 2
            else:
                i = 1
        elif queue[0] == 's':
            if queue[1] == '=':
                i = 2
            else:
                i = 1
        elif queue[0] == 'z':
            if queue[1] == '=':
                i = 2
            else:
                i = 1
        else:
            i = 1
    else:
        i = 1
        
    cnt += 1        
    for _ in range(i):
        queue.popleft()

print(cnt)
