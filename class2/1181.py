import sys
input = sys.stdin.readline

n = int(input())
lst = [input().rstrip() for _ in range(n)]
lst = list(set(lst))    # set(lst)로 중복 삭제, 딕셔너리 형태로 출력

lst.sort(key=lambda x: (len(x), x))

for j in lst:
    print(j)