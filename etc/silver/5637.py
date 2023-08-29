import sys
import re
input = sys.stdin.readline

w = ''
flag = 1
while flag:
    tmp = input().split()
    for i in tmp:
        i = re.sub(r"[^0-9a-zA-Z\-]", "", i)
        # re.sub(pattern, replacement, string)은 string에서 정규표현식의 pattern과 일치하는 내용을 replacement로 변경
        # 정규표현식 앞 ^ 반드시 추가하기
        if i == 'E-N-D':
            flag = 0
            break
        if len(i) > len(w):
            w = i
print(w.lower())