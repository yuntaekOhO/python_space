from collections import deque
list = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
visit = [[False for i in range(5)] for j in range(5)]
px = [1,-1,0,0]
py = [0,0,1,-1]

def bfs(arr,x,y,visit):
    visit[x][y] = True
    q = deque()
    q.append((x,y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            ax = x + px[i]
            ay = y + py[i]
            if visit[ax][ay]==False and arr[ax][ay]==0:
                arr[ax][ay] = 1
                visit[ax][ay] = True
                q.append((ax,ay))
    return print(arr)

bfs(list,0,0,visit)