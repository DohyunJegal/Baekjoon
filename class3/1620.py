import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lstN = {}
lstL = {}
# lstN = 번호: 이름 딕셔너리
# lstL = 이름: 번호 딕셔너리

for i in range(1, n+1):
    tmp = input().rstrip()
    lstN[i] = tmp
    lstL[tmp] = i

for _ in range(m):
    tmp = input().rstrip()
    if tmp.isdigit():
        print(lstN.get(int(tmp)))
    else:
        print(lstL.get(tmp))