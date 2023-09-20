import sys
input = sys.stdin.readline

while True:
    i = input().rstrip()
    if i == "END":
        break
    else:
        print(i[::-1])