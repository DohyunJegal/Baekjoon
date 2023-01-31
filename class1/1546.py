n = int(input())
lst = list(map(int, input().split()))

max_score = max(lst)

new_lst = []
for i in lst:
    new_lst.append(i / max_score * 100)

print(sum(new_lst)/n)

