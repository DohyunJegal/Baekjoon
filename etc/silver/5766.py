import sys
input = sys.stdin.readline

while(True):
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    score = [list(map(int, input().split())) for _ in range(n)]
    rank = {}
    for i in score:
        for j in i:
            if j not in rank:
                rank[j] = 1
            else:
                rank[j] += 1
    rank = sorted(rank.items(), key=lambda x: x[0])
    rank = sorted(rank, key=lambda x: -x[1])

    temp = rank[0][1]
    for i in rank:
        if temp != i[1]:
            temp = i[1]
            break
    for j in rank:
        if j[1] == temp:
            print(j[0], end=' ')
    print('')