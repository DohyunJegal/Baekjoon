import sys
input = sys.stdin.readline

# round(n)으로 푸는 경우 5사5입(앞자리가 홀수면 올리고 앞자리가 짝수면 버림) 적용
def r(n):
    return int(n)+(1 if n-int(n)>=0.5 else 0)

n = int(input())
if n == 0:
    print(0)
else:
    lst = [int(input()) for _ in range(n)]
    rn = r(n*0.15)
    if rn != 0:
        lst = sorted(lst)[rn:-rn]
    print(r(sum(lst)/len(lst)))