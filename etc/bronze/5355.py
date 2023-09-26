import sys
input = sys.stdin.readline

for _ in range(int(input())):
    T = input().split()
    res = float(T[0])
    for i in range(1, len(T)):
        if T[i] == '@':
            res *= 3
        elif T[i] == '%':
            res += 5
        elif T[i] == '#':
            res -= 7
    print(f'{res:.2f}')