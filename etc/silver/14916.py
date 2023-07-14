import sys
input = sys.stdin.readline

n = int(input())
d = [0, -1, 1, -1, 2]
if n<5:
    print(d[n])
else:
    if n%5==0:
        print(n//5)
    else:
        if (n%5)%2==0:
            print(((n%5)//2)+(n//5))
        else:
            print((((n%5)+5)//2)+((n//5)-1))