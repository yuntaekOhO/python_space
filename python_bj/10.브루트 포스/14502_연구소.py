"""
0:안전지대, 1:벽, 2:바이러스
벽을 3개를 놨을 때 안전지대가 가장 많은 경우의 안전지대(0)의 개수
벽이 아닌 곳(0)에 벽을 순서대로 놓고 바이러스를 확산시켰을 때 0의 갯수가 가장 많은 경우를 구한다
"""
#예제입력 통과
#시간초과 : 재귀함수 때문인 듯?
#함수의 인자를 통해 리스트를 전달하고 함수 내에서 값을 변경하면 
#원래의 리스트의 값도 변경되는데
#그 해결 방법으로 copy module의 deepcopy(list)를 사용
# * copy()함수는 이차원 이상의 리스트처럼 내부의 또다른 객체까지 복사하지 못한다. = 1차원일 때만 사용
# copy module이 아닌 파이썬의 기본적인 클래스들이 갖는 copy() 메서드 사용해도 됨 = list도 copy()를 보유함 => list.copy()
# 그외 슬라이싱[:]으로 할당 list(원본) 등등 가능  **deepcopy()가 여러 방법들 중 가장 느리고 슬라이싱[:]이 가장 빠르다
#https://crackerjacks.tistory.com/14 
#https://velog.io/@emplam27/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%A6%AC%EC%8A%A4%ED%8A%B8%EC%9D%98-%EA%B9%8A%EC%9D%80%EB%B3%B5%EC%82%AC%EB%8A%94-deepcopy%EA%B0%80-%EB%B9%A0%EB%A5%BC%EA%B9%8C-slicing%EC%9D%B4-%EB%B9%A0%EB%A5%BC%EA%B9%8C
"""
파이썬에서 객체를 복사할 경우 두가지 경우가 존재함. (ps. Mutable, Immutable)
1.얕은복사
    = 로 값을 대입하는 경우
    리스트의 경우 = 로 값 대입하면 리스트의 '주소'를 참조하기 때문에
    값을 변경,수정할 경우 원본 배열과 복사한 배열이 동일하게 변경이 적용
2.깊은복사
    객체 자체를 새롭게 만드는 행위.

"""
#[pypy3 통과!!]
from collections import deque
import queue
import copy

n, m = map(int, input().split())
inputs = [list(map(int, input().split())) for _ in range(n)]

#상하좌우 이동
px = [-1,1,0,0]
py = [0,0,-1,1]

result = list()

#벽(1)을 세우는 재귀함수
def dfs(arr,i):
    global result
    #종료조건
    if i > 3:
        safe = 0
        q, w = 0, 0
        #2차원 리스트를 module로 깊은 복사 *가장 느림
        #arr2 = copy.deepcopy(arr)
        #2차원 리스트를 슬라이싱으로 깊은복사 *비교적 빠름
        arr2 = [item[:] for item in arr]
        #바이러스(2) 찾기
        for j in range(n):
            for k in range(m):
                if arr2[j][k] == 2:
                    #바이러스를 모두 확산시킨 배열을 temp에 저장
                    temp = virus(arr2,j,k)
        #temp에 안전지대(0)의 개수 세기
        for a in range(n):
            safe += temp[a].count(0)
        #모든 케이스의 안전지대의 수 result에 저장
        result.append(safe)
        return
    for x in range(n):
        for y in range(m):
            if arr[x][y] == 0:
                arr[x][y] = 1
                dfs(arr,i+1)
                arr[x][y] = 0
            
#바이러스(2)를 확산시키는 함수
def virus(arr,x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        #popleft()의 시간복잡도 = O(1)
        #popleft()는 가장 첫번째 들어간 요소를 빼내는 것
        #list의 pop(0)과 같아보이지만 pop(0)의 시간복잡도는 O(n)
        #이렇게 직접 인덱스를 지정한 경우는 O(n)이지만
        #pop()으로 인덱스 없이 사용한 경우(가장 뒤의 요소를 빼내는 경우)는 O(1)이다
        x, y = queue.popleft()
        for k in range(4):
            fx = x + px[k]
            fy = y + py[k]
            #상하좌우 중 이동할 수 없는 경우(값이 없는 경우)
            if fx < 0 or fx >= n or fy < 0 or fy >= m:
                continue
            #벽을 놓을 수 없는 경우 (벽(1)인 경우 또는 바이러스(2)인 경우)
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