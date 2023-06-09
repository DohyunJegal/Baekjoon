import sys
input = sys.stdin.readline

home = list(map(int, input().split()))
away = list(map(int, input().split()))
home_score, away_score, res = 0, 0, 0

for i in range(9):
    home_score += home[i]
    if home_score > away_score:
        res = 1
    away_score += away[i]

if res and away_score > home_score:
    print('Yes')
else:
    print('No')
