word = input().lower()
w_list = list(set(word))
cnt = []

for i in w_list:
    tmp = word.count(i)
    cnt.append(tmp)

if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(w_list[cnt.index(max(cnt))].upper())