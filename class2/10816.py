import sys
input = sys.stdin.readline

n = int(input())
arrA = list(input().split())
card = {}
# i in list는 O(n), i in dict는 O(1)이므로 딕셔너리 사용
for i in arrA:
    if i in card:
        card[i] += 1
    else:
        card[i] = 1

m = int(input())
arrB = list(input().split())
for j in arrB:
    if j in card:
        print(card[j], end=' ')
    else:
        print('0', end=' ')