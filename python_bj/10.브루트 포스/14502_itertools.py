from collections import deque
from itertools import combinations
import copy
#from unittest import result

n, m = map(int, input().split())

graphOrigin = [list(map(int,input().split())) for _ in range(n)]

queue = deque()
queue2 = deque()

for i in range(n):
    for j in range(m):
        #원본에서 0이 위치한 좌표 queue에 저장
        if graphOrigin[i][j] == 0:
            queue.append((i, j))
        #원본에서 2가 위치한 좌표 queue2에 저장
        if graphOrigin[i][j] == 2:
            queue2.append((i, j))

combi = list(combinations(queue, 3))

#graph = []
graph = copy.deepcopy(graphOrigin)

def makeWall(count):
    if count == 3:
        bfs()
        return
    for i in range(0, len(combi)):
        for j in range(3):
            graph[combi[i][j][0]][combi[i][j][1]] = 1
            count += 1
    print('count',count)
            
                

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    graph = copy.deepcopy(graphOrigin)
    queue2.append((x, y))
    while queue2:
        x, y = queue2.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 1:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                queue2.append((nx, ny))

    global result
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                count += 1

    result = max(result, count)

result = 0
makeWall(0)
#print(len(queue))
print('graphOrigin :',graphOrigin)
print('graph:',graph)
print('combi[0]:',combi[0])
print('result',result)



