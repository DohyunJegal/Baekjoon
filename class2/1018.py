import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(input())
c_lst = []

# 기존 체스판을 전체 체크
for i in range(N-7):
    for j in range(M-7):
        # 8*8로 자른 체스판이 W로 시작하는 경우
        countW = 0
        # 8*8로 자른 체스판이 B로 시작하는 경우
        countB = 0

        # 8*8로 자른 체스판과 기존 체스판 비교
        for a in range(i, i+8):
            for b in range(j, j+8):
                # a+b가 짝수라면 시작점의 색과 동일
                if (a+b) % 2 == 0:
                    if lst[a][b] != 'W':
                        countW += 1
                    if lst[a][b] != 'B':
                        countB += 1
                else:
                    if lst[a][b] != 'B':
                        countW += 1
                    if lst[a][b] != 'W':
                        countB += 1

        c_lst.append(min(countW, countB))

print(min(c_lst))