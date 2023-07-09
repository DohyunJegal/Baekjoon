import sys
input = sys.stdin.readline

while True:
    try:
        n = int(input())
    except:
        break

    o, cnt = 1, 1
    while o%n!=0:
        o = o*10+1
        cnt+=1
    print(cnt)
