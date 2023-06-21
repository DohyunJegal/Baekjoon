import sys
input = sys.stdin.readline

def func(g):
    if g == 'A+':
        return 4.5
    elif g == 'A0':
        return 4.0
    elif g == 'B+':
        return 3.5
    elif g == 'B0':
        return 3.0
    elif g == 'C+':
        return 2.5
    elif g == 'C0':
        return 2.0
    elif g == 'D+':
        return 1.5
    elif g == 'D0':
        return 1.0
    else:
        return 0.0

sum = 0
sub = 0
for _ in range(20):
    s = list(input().split())
    if s[2] != 'P':
        sum += float(s[1])*func(s[2])
        sub += float(s[1])
print(f'{sum/sub:.6f}')
