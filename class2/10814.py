import sys
input = sys.stdin.readline

n = int(input())
lst = []

for _ in range(n):
    lst.append(list(input().split()))

lst.sort(key=lambda x:int(x[0]))
# int(x[0])을 해주지 않으면 9 10 정렬 시 10 9로 정렬됨

for i in lst:
    print(i[0], i[1])