import sys
input = sys.stdin.readline

n, m = map(int, input().split())
p_lst = []
e_lst = []
for i in range(m):
    package, each = map(int, input().split())
    p_lst.append(package)
    e_lst.append(each)
res = 0

while n:
    if n >= 6:
        res += min(min(p_lst), min(e_lst)*6)
        n -= 6
    else:
        res += min(p_lst) if min(p_lst) < min(e_lst)*n else min(e_lst)*n
        n = 0

print(res)