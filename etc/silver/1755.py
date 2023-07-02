import sys
input = sys.stdin.readline

eng = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
lst = []

m, n = map(int, input().split())
for i in range(m, n+1):
    number = list(map(int, str(i)))
    num_chr = ''
    for j in number:
        num_chr += eng[j]
    lst.append((num_chr, i))

for k in range(len(sorted(lst))):
    if k != 0 and k % 10 == 0:
        print()
    print(sorted(lst)[k][1], end=' ')
