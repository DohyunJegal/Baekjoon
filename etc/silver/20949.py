import sys
input = sys.stdin.readline

lst = []
for i in range(int(input())):
    w, h = map(int, input().split())
    lst.append(((((w**2)+(h**2))**(1/2))/77, i+1))
lst.sort(key=lambda x: x[1])
lst.sort(key=lambda x:-x[0])

for j in lst:
    print(j[1])