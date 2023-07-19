import sys
input = sys.stdin.readline

lst = []
for _ in range(int(input())):
    lst.append(int(input()))
lst.sort()

res = 0
while len(lst)>2:
    res += lst.pop() + lst.pop()
    lst.pop()
res += sum(lst)
print(res)
