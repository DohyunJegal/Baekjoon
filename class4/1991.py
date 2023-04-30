import sys
input = sys.stdin.readline

def preorder(i):
    print(lst[i][0], end='')
    if lst[i][1] != '.':
        preorder(ord(lst[i][1])-65)
    if lst[i][2] != '.':
        preorder(ord(lst[i][2])-65)

def inorder(i):
    if lst[i][1] != '.':
        inorder(ord(lst[i][1])-65)
    print(lst[i][0], end='')
    if lst[i][2] != '.':
        inorder(ord(lst[i][2])-65)

def postorder(i):
    if lst[i][1] != '.':
        postorder(ord(lst[i][1])-65)
    if lst[i][2] != '.':
        postorder(ord(lst[i][2])-65)
    print(lst[i][0], end='')

n = int(input())
lst = []
for _ in range(n):
    lst.append(input().split())
lst.sort()

preorder(0)
print('')
inorder(0)
print('')
postorder(0)
