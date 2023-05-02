import sys
input = sys.stdin.readline

# A^(m+n) = (A^m)*(A^n)
# (A*B)%C = (A%C)*(B%C)%C
# a=10 , b=11 , c=12인 경우
# 10^11%12 = ((10^5)%12*(10^5)%12*10)%12 = ((10^2)%12*(10^2)%12*10)%12*(10^2)%12*(10^2)%12*10)%12*10)%12
def divide(a, b):
    if b == 1:
        return a%c
    else:
        tmp = divide(a, b//2)
        if b%2 == 0:
            return (tmp*tmp)%c
        else:
            return (tmp*tmp*a)%c

a, b, c = map(int, input().split())
print(divide(a,b))
