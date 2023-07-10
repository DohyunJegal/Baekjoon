import sys
input = sys.stdin.readline

for i in range(int(input())):
    n = int(input())
    note1 = set(map(int, input().split()))
    m = int(input())
    note2 = list(map(int, input().split()))

    for j in note2:
        print(1 if j in note1 else 0)
