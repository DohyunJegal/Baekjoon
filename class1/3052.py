lst = []
for i in range(10):
    n = int(input()) % 42
    lst.append(n)
print(len(set(lst) & set(lst)))