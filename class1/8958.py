n = int(input())
for _ in range(n):
    s = list(input())
    score = 0
    combo = 0
    for i in s:
        if i == "O":
            combo += 1
            score += combo
        else:
            combo = 0
    print(score)