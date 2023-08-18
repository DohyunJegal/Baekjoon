n = int(input())
lst = sorted(list(map(int, input().split())))
print(lst[n//2-1] if n % 2 == 0 else lst[n//2])