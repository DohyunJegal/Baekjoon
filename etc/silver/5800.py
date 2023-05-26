import sys
input = sys.stdin.readline

k = int(input())
for i in range(1, k+1):
    lst = list(map(int, input().split()))
    del lst[0]
    lst.sort()

    gap = 0
    for j in range(len(lst)-1):
        if gap < lst[j+1]-lst[j]:
            gap = lst[j+1]-lst[j]

    print('Class', i)
    print('Max', str(lst[-1])+',', 'Min', str(lst[0])+',', 'Largest gap', gap)