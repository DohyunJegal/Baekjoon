import sys
input = sys.stdin.readline

n = int(input())
res = 0

while True:
    if n % 5 == 0:
        res += n // 5
        print(res)
        break
    elif n < 3:
        print('-1')
        break
    else:
        n -= 3
        res += 1