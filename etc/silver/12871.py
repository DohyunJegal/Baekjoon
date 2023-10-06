import sys
input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()
ts, tt = '', ''

for _ in range(len(t)):
    ts += s
for _ in range(len(s)):
    tt += t

print(1 if ts == tt else 0)