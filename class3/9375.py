import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    m = int(input())
    lst = {}
    res = 1
    for _ in range(m):
        c_name, c_type = input().split()
        if c_type not in lst:
            lst[c_type] = 1
        else:
            lst[c_type] += 1
    for i in lst:
        # 한 종류의 의상을 착용하지 않는 경우 +1
        res *= lst.get(i)+1
    # 모두 입지 않은 경우 제외
    print(res-1)