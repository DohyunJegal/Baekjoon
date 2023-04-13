import sys
import math
input = sys.stdin.readline

lst = list(map(int, input().rstrip()))
cnt = list(lst.count(i) for i in range(10))
cnt[6] = cnt[9] = math.ceil((cnt[6]+cnt[9])/2)
print(max(cnt))