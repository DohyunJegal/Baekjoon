n = int(input())
r = cnt = 1    # r = 방 갯수, cnt = 반복 횟수
while n > r:
    r += cnt * 6    # 6의 배수 만큼 증가
    cnt += 1
print(cnt)