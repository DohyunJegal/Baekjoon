import sys
input = sys.stdin.readline

s = input().rstrip()
n = int(input())
words = {input().rstrip() for _ in range(n)}

for i in range(26):
    temp = ''
    for j in s:
        temp += chr(((ord(j)-97+i)%26)+97)
    for k in words:
        if k in temp:
            print(temp)
            exit(0)