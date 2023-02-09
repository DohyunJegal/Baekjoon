import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
res = 0

for i in lst:
    count = 0
    if i == 1:
        continue
    # 1은 소수가 아니기 때문에
    for j in range(1, i):
        if i % j == 0:
            count += 1
    if count == 1:
        res += 1
print(res)