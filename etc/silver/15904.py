import sys
input = sys.stdin.readline

s = input().rstrip()
cnt = 0
for i in s:
    if cnt == 0 and i == 'U':
        cnt = 1
    if cnt == 1 and i == 'C':
        cnt = 2
    if cnt == 2 and i == 'P':
        cnt = 3
    if cnt == 3 and i == 'C':
        cnt = 4
        break
        
print('I love UCPC' if cnt == 4 else 'I hate UCPC')
