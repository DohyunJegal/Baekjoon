import sys
import heapq

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    minQ, maxQ = [], []
    # heapq는 heap 구조를 유지하지만 정렬되어 있는 상태가 아님
    # 그렇기에 원소에 ID를 부여하여 해당 원소가 존재하는지 판별이 필요
    visited = [0]*n

    for i in range(n):
        k = input().split()
        if k[0] == 'I':
            heapq.heappush(minQ, (int(k[1]), i))
            heapq.heappush(maxQ, (-int(k[1]), i))
            visited[i] = 1
        else:
            if k[1] == '1':
                # 반복문을 통해 최소힙에서 삭제된 정수 제거
                while maxQ and visited[maxQ[0][1]] == 0:
                    heapq.heappop(maxQ)
                if maxQ:
                    visited[maxQ[0][1]] = 0
                    heapq.heappop(maxQ)
            else:
                # 반복문을 통해 최대힙에서 삭제된 정수 제거
                while minQ and visited[minQ[0][1]] == 0:
                    heapq.heappop(minQ)
                if minQ:
                    visited[minQ[0][1]] = 0
                    heapq.heappop(minQ)

    # 정수가 없을 때의 예외처리
    if 1 not in visited:
        print('EMPTY')
    else:
        # 제거되지 못한 정수들 제거
        while maxQ and visited[maxQ[0][1]] == 0:
            heapq.heappop(maxQ)
        while minQ and visited[minQ[0][1]] == 0:
            heapq.heappop(minQ)
        print(-maxQ[0][0], minQ[0][0])