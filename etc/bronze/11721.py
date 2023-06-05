import sys
input = sys.stdin.readline

n = list(input().rstrip())
cnt = 0
for i in range(len(n)):
    print(n[i], end='')
    cnt += 1
    if cnt == 10:
        print('')
        cnt = 0
