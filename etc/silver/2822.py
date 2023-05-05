import sys
input = sys.stdin.readline

lst = []
for i in range(8):
  lst.append((int(input()), i+1))
lst.sort(reverse=True)

s = 0
r = []
for j in range(5):
  s += lst[j][0]
  r.append(lst[j][1])
r.sort()
  
print(s)
for k in r:
  print(k, end=' ')
