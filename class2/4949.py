import sys
from collections import deque

input = sys.stdin.readline

while True:
    str = input().rstrip()
    q = []

    if str == ".":
        break

    for i in str:
        if i == '(' or i == '[':
            q.append(i)
        elif i == ')':
            if len(q) > 0 and q[-1] == '(':
                q.pop()
            else:
                q = ['no']
                break
        elif i == ']':
            if len(q) > 0 and q[-1] == '[':
                q.pop()
            else:
                q = ['no']
                break
    if len(q) == 0:
        print('yes')
    else:
        print('no')