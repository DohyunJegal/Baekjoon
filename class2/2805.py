import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))
tall = max(trees)
short = 1

while short <= tall:
    cut = 0
    mid = (tall+short)//2
    for i in trees:
        if i >= mid:
            cut += i-mid
    if cut >= m:
        short = mid+1
    else:
        tall = mid-1
print(tall)