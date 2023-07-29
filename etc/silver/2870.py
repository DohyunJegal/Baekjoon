import sys
import re
input = sys.stdin.readline

res = []
for _ in range(int(input())):
    tmp = input().rstrip()
    nums = re.findall(r'\d+', tmp)
    for i in nums:
        res.append(int(i))
res.sort()
for j in res:
    print(j)