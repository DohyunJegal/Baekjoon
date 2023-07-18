import sys
input = sys.stdin.readline

a, p = map(int, input().split())
lst = [a]

while True:
    tmp = 0
    for i in str(lst[-1]):
        tmp += int(i)**p
    if tmp in lst:
        break
    else:
        lst.append(tmp)

print(lst.index(tmp))
