"""
[브루트 포스 4번]
지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다. 
어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.
체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 
구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 
따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.
보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 
당연히 8*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다. 
둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.

첫째 줄에 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.
"""
import sys
 
N, M = map(int, sys.stdin.readline().split())
 
board = []
white_first = []
black_first = []
 
for _ in range(N):
    row = sys.stdin.readline().replace("\n", "") #여러 줄 입력
    board.append([i for i in row]) #2단 리스트로 저장
 
initial_color = board[0][0] # 좌상단 첫번째 칸 색 초기화
 
# 흰색으로 시작하는 체스판을 만들 경우
for index, row in enumerate(board):
    painting = [] #흰색으로 시작하는 경우 색을 바꿔야하는 칸의 수 저장할 리스트
    if index % 2 == 0: current_color = "W" #짝수 인덱스는 White
    else: current_color = "B" #홀수 인덱스는 Black
 
    for value in row: #인덱스에 해당하는 값(W,B) 찾기
        if value == current_color: painting.append(0) #조건에 맞는 색깔이면 0
        else: painting.append(1) #바꿔 칠해야하는 색깔이면 1
        
        if current_color == "W": current_color = "B" #다음 칸 검사하기 위해 변경
        else: current_color = "W"
    white_first.append(painting) #0,1 저장
 
# 검은색으로 시작하는 체스판을 만들 경우
for index, row in enumerate(board):
    painting = []
    if index % 2 == 0: current_color = "B"
    else: current_color = "W"
 
    for value in row:
        if value == current_color: painting.append(0)
        else: painting.append(1)
        
        if current_color == "W": current_color = "B"
        else: current_color = "W"
    black_first.append(painting)
 
# 최솟값을 초기화 할 때, 보드의 최대 크기인 50*50 = 2500으로 한다.
min_count = 2500
for i in range(N-7): # 8*8 체스판을 만들어야 할 때 NxM 크기에서 자를 수 있는 경우의 수 (N-7)*(M-7)가지
    rows = white_first[i:i+8] #좌상단 첫번째가 하얀색으로 시작하는 경우일 때 다시 색칠해야 하는 횟수 리스트를 rows에 저장
    for j in range(M-7):
        paint = 0
        for row in rows:
            paint += sum(row[j:j+8]) # 라인 단위로 다시 색칠해야 하는 횟수 중첩
        if paint < min_count: min_count = paint
 
for i in range(N-7):
    rows = black_first[i:i+8]
    for j in range(M-7):
        paint = 0
        for row in rows:
            paint += sum(row[j:j+8])
        if paint < min_count: min_count = paint
 
print(min_count)