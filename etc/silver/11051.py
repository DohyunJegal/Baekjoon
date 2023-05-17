import sys
import math
from fractions import Fraction
input = sys.stdin.readline

n, k = map(int, input().split())
print(int(Fraction(math.factorial(n), math.factorial(k)*math.factorial(n-k))%10007))