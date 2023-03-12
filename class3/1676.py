import sys
import math
input = sys.stdin.readline

n = int(input())
lst = list(map(int, str(math.factorial(n))))
tmp = cnt = 0
point = -1

while tmp == 0:
    tmp = lst[point]
    if tmp == 0:
        cnt += 1
    point -= 1

print(cnt)