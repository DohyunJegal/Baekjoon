import sys
input = sys.stdin.readline

n = int(input())
queue = []

for _ in range(n):
    comm = input().split()

    if comm[0] == 'push':
        queue.append(comm[1])
    elif comm[0] == 'pop':
        if len(queue) != 0:
            print(queue[0])
            del queue[0]
        else:
            print('-1')
    elif comm[0] == 'size':
        print(len(queue))
    elif comm[0] == 'empty':
        print('1' if len(queue) == 0 else '0')
    elif comm[0] == 'front':
        print('-1' if len(queue) == 0 else queue[0])
    elif comm[0] == 'back':
        print('-1' if len(queue) == 0 else queue[-1])