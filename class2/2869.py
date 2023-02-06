import sys
import math
input = sys.stdin.readline

up, down, length = map(int, input().split())

print(math.ceil((length - down) / (up - down)))
# 낮에 도착하면 내려갈 이유가 없기 때문에 length - down