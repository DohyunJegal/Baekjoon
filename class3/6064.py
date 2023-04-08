import sys
input = sys.stdin.readline

def cnt(m, n, x, y):
    t = x   # x를 고정하여 찾는 횟수 줄이기
    while t <= m*n:
        if (t-x)%m == 0 and (t-y)%n == 0:
            return t
        t += m  # m번마다 t가 등장
    return -1

for _ in range(int(input())):
    m, n, x, y = map(int, input().split())
    print(cnt(m, n, x, y))