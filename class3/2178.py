import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

def bfs(x, y):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if 0 <= tx < n and 0 <= ty < m and graph[tx][ty] == 1:
                graph[tx][ty] = graph[x][y] + 1
                queue.append((tx, ty))

    return graph[n-1][m-1]

print(bfs(0, 0))