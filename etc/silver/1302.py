import sys
input = sys.stdin.readline

lst = {}
for _ in range(int(input())):
    book = input().rstrip()
    if book in lst:
        lst[book] += 1
    else:
        lst[book] = 1
print(max(sorted(lst), key=lst.get))
