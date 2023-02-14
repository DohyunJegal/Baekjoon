import sys
input = sys.stdin.readline

r = int(input())

for _ in range(r):
    k = int(input())    # 층
    n = int(input())    # 호

    lst = list(j for j in range(1, n+1))
    for _ in range(k):
        for i in range(1, n):   # xx1호 제외
            lst[i] += lst[i-1]

    print(lst[-1])