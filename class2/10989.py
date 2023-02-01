import sys
input = sys.stdin.readline()
n = int(input())
lst = [0] * 10001
for _ in range(n):
    lst[int(input())] += 1
for i in range(10001):
    if lst[i] != 0:
        for k in range(lst[i]):
            print(i)

# 기존 코드
#   n = int(input())
#   lst = []
#   for _ in range(n):
#       lst.append(int(input()))
#   lst.sort()
#   for i in range(n):
#       print(lst[i])
#   >> 메모리 초과 ( 제한 : 8MB )
# 팁
#   input()   >   import sys
#                 input = sys.stdin.readline
#                 개행문자 제거를 위해 형변환 사용하기