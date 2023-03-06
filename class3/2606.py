import sys
from collections import deque

input = sys.stdin.readline

c = int(input())
n = int(input())
visited = deque([0]*(c+1))
graph = deque([0]*(c+1) for _ in range(c+1))
for _ in range(n):
    s, e = map(int, input().split())
    graph[s][e] = graph[e][s] = 1

def dfs(v):
    visited[v] = 1
    for i in range(1, c+1):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i)

dfs(1)
print(sum(visited)-1)