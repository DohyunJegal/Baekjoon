import sys
input = sys.stdin.readline

cnt, res = {}, 0
for _ in range(int(input())):
    s = input().rstrip()
    if s == 'ENTER':
        res += len(cnt)
        cnt = {}
    else:
        if s not in cnt:
            cnt[s] = 1
res += len(cnt)
print(res)