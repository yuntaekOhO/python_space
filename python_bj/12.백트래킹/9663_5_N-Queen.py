"""
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

첫째 줄에 N이 주어진다. (1 ≤ N < 15)

첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.
"""
# answer = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596]
# print(answer[int(input())])

# 퀸 : 가로, 세로, 대각선으로 이동

n = int(input())
queen = [0] * n
result = 0

#열, 대각선 상에 있는지 체크
def isAdjecent(idx):
    for i in range(idx): #행
        if queen[idx] == queen[i] or abs(queen[idx] - queen[i]) == idx - i:
            return False
    return True
def dfs(idx):
    if idx == n:
        global result
        result += 1
        return
    for i in range(n):
        queen[idx] = i  #열
        if isAdjecent(idx):
            dfs(idx + 1)
dfs(0)
print(result)

# n = int(input())
# cnt = 0
# col = [0] * (n+1)
# visited =  [False] * (n+1)
# def n_queens(i, col):
#     if(promising(i, col)):
#         if(i == n):
#             global cnt
#             cnt += 1
#             return
#         else:
#             for j in range(1, n+1):
#                 visited[j] = True
#                 col[i+1] = j
#                 n_queens(i+1, col)
#                 visited[j] = False

# def promising(i, col):
#     flag = True
#     for x in range(i+1):
#         #아래 조건에 들어가지 않아야 퀸의 자리
#         #    같은 열 체크           대각선 체크
#         if(col[i]==col[x] or abs(col[i]-col[x])==(i-x)):
#             flag = False
#     return flag #True 반환하면 유망함, False 반환하면 pruned함 (더이상 찾을 가치 없음 -> 백트랙 함)

# n_queens(0, col)
# print(cnt)