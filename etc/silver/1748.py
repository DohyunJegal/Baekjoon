import sys
input = sys.stdin.readline

n = int(input())
length = len(str(n)) - 1
res, cnt = 0, 0

# 1~9 9개 -> 9*1 = 9개 필요, 10~99 90개 -> 90*2 = 180개 필요, 100~999개 900개 -> 900*3 = 2700개 필요 ...
while cnt < length:
    res += 9*(10**cnt)*(cnt+1)
    cnt += 1
res += (n-(10**length)+1)*(length+1)

print(res)