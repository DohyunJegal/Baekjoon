import sys
input = sys.stdin.readline

while True:
    n = input().rstrip()
    if n == "0":
        break
    else:
        print('yes' if n == n[::-1] else 'no')

# 뒤집었을 때 원래의 값과 같으면 팰린드롬수