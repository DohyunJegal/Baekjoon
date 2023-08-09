import sys
input = sys.stdin.readline

cows = []
for _ in range(int(input())):
    cows.append(list(map(int, input().split())))
cows.sort(key=lambda x:x[0])

time = 0
for i in cows:
    if i[0] > time:
        time = i[0] + i[1]
    else:
        time += i[1]
print(time)