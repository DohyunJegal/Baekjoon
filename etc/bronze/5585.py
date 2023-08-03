import sys
input = sys.stdin.readline

change = [500, 100, 50, 10, 5, 1]
money = 1000 - int(input())
cnt = 0

for i in change:
    cnt += money//i
    money %= i

print(cnt)