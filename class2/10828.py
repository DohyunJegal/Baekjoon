import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    comm = input().split()

    if comm[0] == 'push':
        stack.append(comm[1])
    elif comm[0] == 'pop':
        if len(stack) != 0:
            print(stack[-1])
            del stack[-1]
        else:
            print('-1')
    elif comm[0] == 'size':
        print(len(stack))
    elif comm[0] == 'empty':
        print('1' if len(stack) == 0 else '0')
    elif comm[0] == 'top':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print('-1')