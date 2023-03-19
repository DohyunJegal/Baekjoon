import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
lst_sum = [0] * (len(nums)+1)
tmp = 1
for a in nums:
    if tmp == 1:
        lst_sum[1] = a
    else:
        lst_sum[tmp] = lst_sum[tmp-1] + a
    tmp += 1

for _ in range(m):
    i, j = map(int, input().split())
    print(lst_sum[j] - lst_sum[i-1])
