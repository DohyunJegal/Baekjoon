import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
T, P = map(int, input().split())
shirt = 0

for i in lst:
    shirt += i//T
    if i % T != 0:
        shirt += 1

print(shirt)
print(N//P, N%P)