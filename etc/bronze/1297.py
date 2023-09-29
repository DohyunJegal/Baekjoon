import sys
input = sys.stdin.readline

d, h, w = map(int, input().split())
r = d/((h**2+w**2)**0.5)
print(int(h*r), int(w*r))
