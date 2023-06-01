import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    koong = [1, 1, 2, 4]
    n = int(input())
    for i in range(4, n+1):
        koong.append(koong[i-1]+koong[i-2]+koong[i-3]+koong[i-4])
    print(koong[n])
