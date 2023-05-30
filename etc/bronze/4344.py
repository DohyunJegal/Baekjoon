import sys
input = sys.stdin.readline

c = int(input())
for _ in range(c):
    lst = list(map(int, input().split()))
    del lst[0]
    avg = float(sum(lst)/len(lst))
    cnt = 0
    for i in lst:
        if i > avg:
            cnt += 1
    print(f'{cnt/len(lst)*100:.3f}%')
