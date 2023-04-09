import sys
input = sys.stdin.readline

# 유클리드 호제법 -> 2609번 문제와 동일
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x < y:
        x, y = y, x

    a, b = x, y
    while b != 0:
        a = a % b
        a, b = b, a

    print(int((x*y)/a))