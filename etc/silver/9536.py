import sys
input = sys.stdin.readline

for _ in range(int(input())):
    tc = list(input().split())
    animals = {}
    res = []
    
    while True:
        tmp = list(input().split())
        if tmp == ['what', 'does', 'the', 'fox', 'say?']:
            for i in tc:
                if i not in animals:
                    res.append(i)
            break
        else:
            animals[tmp[2]] = 1

    for j in res:
        print(j, end=' ')
