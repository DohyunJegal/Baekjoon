import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())
res = 0

while n != 0:
    n -= 1

    # 사분면으로 나눠서 계산
    # 좌상단
    if r < 2**n and c < 2**n:
        # 사분면에 해당되는 칸 수를 결과값에 더해줌
        res += (2**n) * (2**n) * 0
    # 우상단
    elif r < 2**n and c >= 2**n:
        res += (2**n) * (2**n) * 1
        # 줄어든 영역에 맞춰 좌표 보정
        c -= 2**n
    # 좌하단
    elif r >= 2 ** n and c < 2 ** n:
        res += (2**n) * (2**n) * 2
        r -= 2**n
    # 우하단
    else:
        res += (2**n) * (2**n) * 3
        c -= 2**n
        r -= 2**n

print(res)