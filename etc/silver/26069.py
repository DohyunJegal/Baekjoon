import sys
input = sys.stdin.readline

lst = {}
def check(names):
    flag = True if names[0] == 'ChongChong' or names[1] == 'ChongChong' else False
    for i in names:
        if i not in lst:
            lst[i] = 1 if flag == 1 else 0
    if lst[names[0]] == 1 or lst[names[1]] == 1:
        lst[names[0]] = 1
        lst[names[1]] = 1

for _ in range(int(input())):
    check(input().split())
print(sum(lst.values()))