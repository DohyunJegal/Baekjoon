import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)
# 인덱스의 수가 1이 되는데 필요한 연산의 최솟값을 가지는 dp리스트

for i in range(2, n+1):
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])