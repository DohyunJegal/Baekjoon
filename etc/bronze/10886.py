yes, no = 0, 0
for _ in range(int(input())):
    n = int(input())
    if n == 1:
        yes += 1
    else:
        no += 1
print('Junhee is not cute!' if yes < no else 'Junhee is cute!')