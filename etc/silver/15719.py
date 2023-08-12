# [pypy3] 수열에 중복된 숫자 r이 추가된 형태이기 때문에, 수열의 합 - (1부터 n-1까지의 합) = r이다.

import sys
input = sys.stdin.readline

n = int(input())
s = sum(range(1, n))    # 1부터 n-1까지의 합
line = input().rstrip()

tmp, cnt = '', 0
for i in line:
    if i.isdigit():
        tmp += i
    else:
        cnt += int(tmp)
        tmp = ''
cnt += int(tmp) # 마지막에 오는 숫자를 따로 처리

print(cnt-s)