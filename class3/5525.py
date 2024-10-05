import sys
input = sys.stdin.readline

N = int(input())
S = int(input())
M = input().rstrip()
i, res, cnt = 0, 0, 0
while i < S-1:
    if M[i:i+3] == 'IOI':
        i += 2
        cnt += 1
        if cnt == N:
            res += 1
            cnt -= 1
    else:
        i += 1
        cnt = 0
print(res)