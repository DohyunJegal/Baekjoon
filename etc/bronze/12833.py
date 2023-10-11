a, b, c = map(int, input().split())
r = [a^b, (a^b)^b]
print(r[0] if c%2!=0 else r[1])
# a = 1101, b = 1011일 때, xor 연산을 계속하면 0110 1101 0110 1101 ...