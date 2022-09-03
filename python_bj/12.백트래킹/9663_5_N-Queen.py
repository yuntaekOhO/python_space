"""
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

첫째 줄에 N이 주어진다. (1 ≤ N < 15)

첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.
"""
# 퀸 : 가로, 세로, 대각선으로 이동

# n = int(input())
# cnt = 0

n = int(input())
cnt = 0
col = [0] * (n+1)

def n_queens(i, col):
    #n = len(col) - 1
    if(promising(i, col)):
        if(i == n):
            global cnt
            cnt += 1 
        else:
            for j in range(1, n+1):
                col[i+1] = j
                n_queens(i+1, col)

def promising(i, col):
    k = 1
    flag = True
    while(k<i and flag):
        #아래 조건에 들어가지 않아야 퀸의 자리
        #    같은 열 체크           대각선 체크
        if(col[i]==col[k] or abs(col[i]-col[k])==(i-k)):
            flag = False
        k += 1
    return flag #True 반환하면 유망함, False 반환하면 pruned함 (더이상 찾을 가치 없음 -> 백트랙 함)

n_queens(0, col)
print(cnt)