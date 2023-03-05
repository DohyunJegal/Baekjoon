import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = deque([0] * (n+1) for _ in range(n+1))
visited_dfs = deque([0] * (n+1))
visited_bfs = deque([0] * (n+1))
for _ in range(m):
    s, e = map(int, input().split())
    graph[s][e] = graph[e][s] = 1

def dfs(v):
    visited_dfs[v] = 1
    print(v, end=' ')
    for i in range(1, n+1):
        if visited_dfs[i] == 0 and graph[v][i] == 1:
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited_bfs[v] = 1

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for j in range(1, n + 1):
            if visited_bfs[j] == 0 and graph[v][j] == 1:
                queue.append(j)
                visited_bfs[j] = 1

dfs(v)
print()
bfs(v)