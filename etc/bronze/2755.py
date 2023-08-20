import sys
input = sys.stdin.readline

cre, res = 0, 0
calc = {"A+": 4.3, "A0": 4.0, "A-": 3.7,
        "B+": 3.3, "B0": 3.0, "B-": 2.7,
        "C+": 2.3, "C0": 2.0, "C-": 1.7,
        "D+": 1.3, "D0": 1.0, "D-": 0.7,
        "F": 0.0}

n = int(input())
for _ in range(n):
    i = input().split()
    cre += int(i[1])
    res += int(i[1])*calc[i[2]]
print("%.2f"%(round(res/cre+10**-10, 2)))   # 사사오입 방지를 위해 10**-10 더하기
