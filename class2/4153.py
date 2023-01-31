while True:
    lst = list(map(int, input().split()))
    lst.sort()
    if sum(lst) == 0:
        break
    else:
        print("right" if lst[2] ** 2 == lst[0] ** 2 + lst[1] ** 2 else "wrong")