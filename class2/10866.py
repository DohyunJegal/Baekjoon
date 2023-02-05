import sys
input = sys.stdin.readline

n = int(input())
deque = []

for _ in range(n):
    comm = input().split()

    if comm[0] == 'push_front':
        deque.insert(0, comm[1])
    elif comm[0] == 'push_back':
        deque.append(comm[1])
    elif comm[0] == 'pop_front':
        if len(deque) != 0:
            print(deque[0])
            del deque[0]
        else:
            print('-1')
    elif comm[0] == 'pop_back':
        if len(deque) != 0:
            print(deque[-1])
            del deque[-1]
        else:
            print('-1')
    elif comm[0] == 'size':
        print(len(deque))
    elif comm[0] == 'empty':
        print('1' if len(deque) == 0 else '0')
    elif comm[0] == 'front':
        print('-1' if len(deque) == 0 else deque[0])
    elif comm[0] == 'back':
        print('-1' if len(deque) == 0 else deque[-1])