import sys
input = sys.stdin.readline

n = int(input())
sp, ep = map(str, input().rstrip().split('*'))
for _ in range(n):
    file = list(map(str, input().rstrip('\n')))
    s, e = ''.join(file[:len(sp)]), ''.join(file[-len(ep):])

    # 파일 이름의 길이가 왼쪽, 오른쪽 패턴의 합보다 작은 경우 일치 불가
    if len(sp) + len(ep) > len(file):
        print('NE')
    else:
        print('DA' if s == sp and e == ep else 'NE')
