from collections import deque

strList = list()
n = int(input())
inputs = []
for i in range(n):
    inputs.append(list(input()))
visited = [[False for i in range(n)] for j in range(n)] 
#print('visited:',visited)
#print('inputs:',inputs)
mx = [-1,1,0,0]
my = [0,0,-1,1]

def bfs(x,y,visited):
    q = deque()
    q.append((x,y))
    #인자로 전달된 위치를 방문 처리
    visited[x][y] = True
    #인자로 전달된 위치의 인접한 곳 탐색
    while q:
        fx, fy = q.popleft()
        for i in range(4):
            px = fx + mx[i]
            py = fy + my[i]
            #그리드의 바깥 무시
            if px<0 or px>=n or py<0 or py>=n:
                continue
            #이미 방문한 곳 무시
            if visited[px][py] == True:
                continue
            #인자로 전달된 위치의 인접한 곳 중에서 아직 방문하지 않았고 최초의 위치의 색상값이 같은 경우
            if visited[px][py] == False and inputs[px][py]==inputs[x][y]:
                visited[px][py] = True
                q.append((px,py))
    #print('visited:',visited)
    return 1

cnt, cnt1 = 0,0
#적록색약이 아닌 경우
for i in range(n):
    for j in range(n):
        if visited[i][j]==False:
            cnt += bfs(i,j,visited)
#적록색약의 경우를 구하기 위해 R을 G로 바꿈
for i in range(n):
    for j in range(n):
        visited[i][j] = False
        if inputs[i][j]=='R':
            inputs[i][j] = 'G'
#적록색약인 경우
for i in range(n):
    for j in range(n):
        if visited[i][j]==False:
            cnt1 += bfs(i,j,visited)
print(cnt,cnt1)
#print(cnt1)
