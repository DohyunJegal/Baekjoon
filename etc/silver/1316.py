import sys
input = sys.stdin.readline

res = []
for _ in range(int(input())):
    word = input().rstrip()
    tmp = {}
    check = 0
    for i in range(len(word)):
        if word[i-1] != word[i] and word[i] in tmp:
            check = 1
            break
        else:
            tmp[word[i]] = 1
    if check == 0:
       res.append(1)
print(res.count(1))