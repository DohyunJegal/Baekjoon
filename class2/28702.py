import sys
input = sys.stdin.readline

lst = [input().rstrip() for _ in range(3)]
res = 0
for i in range(len(lst)):
    if str.isdigit(lst[i]):
        res = int(lst[i])+(3-i)
        break
if res%15 == 0:
    print('FizzBuzz')
elif res%5 == 0:
    print('Buzz')
elif res%3 == 0:
    print('Fizz')
else:
    print(res)