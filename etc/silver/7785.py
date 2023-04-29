import sys
input = sys.stdin.readline

lst = {}
for _ in range(int(input())):
  name, order = map(str, input().split())
  if order == 'enter':
    lst[name] = True
  else:
    del lst[name]
    
for i in sorted(lst, reverse=True):
  print(i)
