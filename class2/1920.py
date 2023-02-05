import sys
input = sys.stdin.readline

a = int(input())
old_lst = list(map(int, input().split()))
old_lst.sort()
b = int(input())
new_lst = list(map(int, input().split()))

for i in new_lst:   # 이진탐색
    first, last, res = 0, len(old_lst)-1, 0
    while first <= last:
        mid = int((first + last)/2)
        if i > old_lst[mid]:
            first = mid + 1
        elif i < old_lst[mid]:
            last = mid - 1
        else:
            res = 1
            break
    print(res)
