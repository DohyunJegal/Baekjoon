import sys
import math
from fractions import Fraction

input = sys.stdin.readline

# 조합: 서로 다른 n개의 물건에서 순서를 생각하지 않고 r개를 택함
# nCr = nCn-r = n!/r!(n-r)!
n, m = map(int, input().split())

# 나눗셈에서 오차가 발생하기 때문에, 나눗셈 대신 fractions 모듈을 이용하여 유리수를 정확하게 다뤄야 함
print(int(Fraction(math.factorial(n), (math.factorial(m)*math.factorial(n-m)))))