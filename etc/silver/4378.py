import sys
input = sys.stdin.readline

keyboard = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;\'ZXCVBNM,./"

while True:
    error = input().rstrip()

    if error == '':
        break
    else:
        res = ''
        for i in error:
            if i == ' ':
                res += ' '
            else:
                res += keyboard[keyboard.index(i)-1]
        print(res)
