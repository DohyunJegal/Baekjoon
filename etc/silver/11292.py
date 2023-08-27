import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break

    people = []
    for _ in range(n):
        tmp = input().split()
        people.append((tmp[0], float(tmp[1])))
    people.sort(key= lambda x: -x[1])

    height = people[0][1]
    res = ''
    for i in people:
        if i[1] == height:
            res += i[0] + ' '
        else:
            break

    print(res)