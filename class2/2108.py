import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))
lst.sort()

# 산술평균
print(round(sum(lst)/n))

# 중앙값
print(lst[len(lst)//2])

# 최빈값
count = {}
for i in lst:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
freq = max(count.values())
freqArr = []
for j in count:
    if count[j] == freq:
        freqArr.append(j)
if len(freqArr) > 1:
    print(freqArr[1])
else:
    print(freqArr[0])

# 범위
print(max(lst)-min(lst))

