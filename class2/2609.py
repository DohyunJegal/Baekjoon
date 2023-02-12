import sys
input = sys.stdin.readline

a, b = map(int, input().split())
if a < b:
    a, b = b, a
tmp_a, tmp_b = a, b

# 유클리드 호제법 사용
# a와 b의 최대공약수 G == a % b의 최대공약수 G' (단, a > b)
while tmp_b != 0:
    tmp_a = tmp_a % tmp_b
    tmp_a, tmp_b = tmp_b, tmp_a

# 최대공약수 GCD
print(tmp_a)
# 최소공배수 LCM
# a == x * gcd(a, b), b == y * gcd(a, b)이기 때문에,
# a로 나눠도 b로 나눠도 나누어 떨어지는 수 중에서 가장 작은 수가 최소공배수 LCM
print(int(a * b / tmp_a))