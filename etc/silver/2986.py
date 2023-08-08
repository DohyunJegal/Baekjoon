import sys
input = sys.stdin.readline

n = int(input())
div = 1
for i in range(2, int(n**(1/2))+1):
    if n%i == 0:
        div = n//i
        break
print(n-div)