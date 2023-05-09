import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
d = [1]*n

for i in range(1, n):
    for j in range(i):
        # lst[i] 이전의 값들 중 가장 큰 값(lst[j])이 있는지 확인하고,
        # 없다면 d[i] = 1, 있다면 d[i] = d[j] + 1
        if lst[i] > lst[j]:
            d[i] = max(d[i], d[j]+1)

print(max(d))