"""
0:안전지대, 1:벽, 2:바이러스
벽을 3개를 놨을 때 안전지대가 가장 많은 경우의 안전지대(0)의 개수
벽이 아닌 곳(0)에 벽을 순서대로 놓고 바이러스를 확산시켰을 때 0의 갯수가 가장 많은 경우를 구한다
"""
#예제입력 통과
#시간초과
from collections import deque
import queue
import copy

n, m = map(int, input().split())
inputs = [list(map(int, input().split())) for _ in range(n)]

#상하좌우 이동
px = [-1,1,0,0]
py = [0,0,-1,1]

result = list()

def dfs(arr,i):
    global result
    if i > 3:
        safe = 0
        q, w = 0, 0
        arr2 = copy.deepcopy(arr)
        for j in range(n):
            for k in range(m):
                if arr[j][k] == 2:
                    q, w = j, k
                    temp = virus(arr2,q,w)
        for a in range(n):
            safe += temp[a].count(0)
        result.append(safe)
        return
    for x in range(n):
        for y in range(m):
            if arr[x][y] == 0:
                arr[x][y] = 1
                dfs(arr,i+1)
                arr[x][y] = 0
            
def virus(arr,x,y):
    #바이러스 확산시켜 보기
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            fx = x + px[k]
            fy = y + py[k]
            #상하좌우 중 이동할 수 없는 경우(값이 없는 경우)
            if fx < 0 or fx >= n or fy < 0 or fy >= m:
                continue
            #벽을 놓을 수 없는 경우 (벽(1)인 경우 또는 바이러스 근원지(2)인 경우)
            if arr[fx][fy] != 0:
                continue
            if arr[fx][fy] == 0:
                queue.append((fx,fy))
                arr[fx][fy] = 2                
    return arr

dfs(inputs,1)
print(max(result))




# def bfs(arr,x,y,w):
#     safe = 0
#     queue = deque()
#     queue.append((x,y))
#     while queue:
#         x, y = queue.popleft() 
#         # if w >= 3 : break
#         #선택된 공간,상하좌우 탐색
#         for i in range(5):
#             nx = x + px[i]
#             ny = y + py[i]
#             #상하좌우 중 이동할 수 없는 경우(값이 없는 경우)
#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue
#             #벽을 놓을 수 없는 경우 (벽(1)인 경우 또는 바이러스 근원지(2)인 경우)
#             if arr[nx][ny] != 0:
#                 continue
#             #벽을 놓을 수 있는 경우 (0인 경우)
#             if arr[nx][ny] == 0:
#                 arr[nx][ny] = 1
#                 w += 1
#                 queue.append((nx,ny))
#                 if w >= 3:
#                     #바이러스 확산시켜 보기
#                     for i in range(n):
#                         for j in range(m):
#                             if arr[i][j] == 2:
#                                 for k in range(5):
#                                     fx = i + px[k]
#                                     fy = j + px[k]
#                                     #상하좌우 중 이동할 수 없는 경우(값이 없는 경우)
#                                     if fx < 0 or fx >= n or fy < 0 or fy >= m:
#                                         continue
#                                     #벽을 놓을 수 없는 경우 (벽(1)인 경우 또는 바이러스 근원지(2)인 경우)
#                                     if arr[fx][fy] != 0:
#                                         continue
#                                     if arr[fx][fy] == 0:
#                                         arr[fx][fy] = 2
#                         safe += arr[i].count(0)
#     return safe

# maxVal = 0
# for i in range(n):
#     for j in range(m):
#         result = bfs(inputs, i, j, 0)
#         maxVal = max(maxVal, result)
# print(maxVal)
#print(type(maxVal), type(result))