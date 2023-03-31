import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    queue = input().rstrip()
    n = int(input())
    x = deque(list(input().rstrip()[1:-1].split(',')))
    if n == 0:
        x = deque([])
    count = err = 0

    for i in queue:
        if i == 'R':
            count += 1
        elif i == 'D':
            if len(x) != 0:
                if count % 2 == 0:
                    x.popleft()
                else:
                    x.pop()
            else:
                err = 1

    if len(x) == 0 and err == 1:
        print('error')
    else:
        if count % 2 == 0:
            print('[' + ','.join(x) + ']')
        else:
            x.reverse()
            print('[' + ','.join(x) + ']')