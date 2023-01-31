l = int(input())  # loop
for _ in range(l):
    h, w, n = map(int, input().split())  # h = 층, w = 각 층의 방, n = 손님 번호
    a = n % h  # 방 번호, aabb 형식
    b = n // h + 1
    if a == 0:
        a = h
        b -= 1
    print(a * 100 + b)