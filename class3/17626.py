# Python3으로 제출 시 시간 초과, PyPy3으로 제출 시 맞았습니다!!
# Python3은 dp가 아닌 브루트포스 알고리즘으로 해결해야 함

import sys
input = sys.stdin.readline

n = int(input())
d = [0]*(n+1)
d[0], d[1] = 0, 1

for i in range(2, n+1):
    # INF 표현
    minVal = 1e9
    j = 1

    # d[n-제곱수]+1 = res, 여기서 제곱수는 n보다 작거나 같은 제곱수
    while j**2 <= i:
        minVal = min(minVal, d[i-(j**2)])
        j += 1

    d[i] = minVal + 1

print(d[n])
