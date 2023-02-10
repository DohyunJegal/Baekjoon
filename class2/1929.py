import sys
input = sys.stdin.readline

a, b = map(int, input().split())

for i in range(a, b+1):
    if i == 1:
        continue
    flag = 0
    for j in range(2, int(i**0.5)+1):
        # 제곱근의 약수를 구하면 이 약수를 포함하는 수 제거 가능
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        print(i)