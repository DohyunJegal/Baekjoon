import sys
input = sys.stdin.readline

n = int(input())
nums = []
for _ in range(n):
    nums.append(input().rstrip())

for i in range(len(nums[0])-1, -1, -1):
    tmp = []
    for j in range(n):
        if nums[j][i:] in tmp:
            break
        else:
            tmp.append(nums[j][i:])
    if len(tmp) == n:
        print(len(tmp[0]))
        break