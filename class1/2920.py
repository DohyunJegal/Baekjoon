lst = list(input().split())
print("ascending" if lst == sorted(lst) else ("descending" if lst == sorted(lst, reverse=True) else "mixed"))