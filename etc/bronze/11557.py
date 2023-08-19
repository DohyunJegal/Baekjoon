import sys
input = sys.stdin.readline

for _ in range(int(input())):
    lst = []
    for _ in range(int(input())):
        name, csp = input().split()
        lst.append([name, int(csp)])
    lst.sort(key=lambda x:-x[1])
    print(lst[0][0])
