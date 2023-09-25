import sys
input = sys.stdin.readline

n = int(input())
lst = map(int, input().split())
for i in lst:
    print(1 if int(i**(1/2))**2 == i else 0, end=" ")
    # 제곱근이 정수인 경우 약수의 개수는 홀수, 제곱근이 정수가 아닌 경우 약수의 개수는 짝수