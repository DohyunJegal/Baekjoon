import sys
input = sys.stdin.readline

n = input().rstrip()
happy, sad = 0, 0
for i in range(len(n)-2):
    if n[i:i+3] == ':-)':
        happy += 1
    elif n[i:i+3] == ':-(':
        sad += 1

if happy > sad:
    print('happy')
elif happy < sad:
    print('sad')
elif (happy or sad) and happy == sad:
    print('unsure')
else:
    print('none')