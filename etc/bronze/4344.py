import sys
input = sys.stdin.readline

# 파이썬 오사오입 문제 해결
def r(v, d):
    return round(v+10**(-len(str(v))-1), d)

c = int(input())
for _ in range(c):
    lst = list(map(int, input().split()))
    del lst[0]
    avg = float(sum(lst)/len(lst))
    cnt = 0
    for i in lst:
        if i > avg:
            cnt += 1
    print(f'{r(cnt/len(lst)*100, 3):.3f}%')
