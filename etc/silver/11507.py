import sys
from collections import deque
input = sys.stdin.readline

def cards():
    print('GRESKA')
    exit()

s = deque(list(input().rstrip()))
card = [{}, {}, {}, {}]
while s:
    tmp = ''
    for _ in range(3):
        tmp += s.popleft()

    if tmp[0] == 'P':
        if tmp[1:] not in card[0]:
            card[0][tmp[1:]] = 1
        else:
            cards()
    elif tmp[0] == 'K':
        if tmp[1:] not in card[1]:
            card[1][tmp[1:]] = 1
        else:
            cards()
    elif tmp[0] == 'H':
        if tmp[1:] not in card[2]:
            card[2][tmp[1:]] = 1
        else:
            cards()
    elif tmp[0] == 'T':
        if tmp[1:] not in card[3]:
            card[3][tmp[1:]] = 1
        else:
            cards()

for i in range(4):
    print(13-len(card[i]), end=' ')