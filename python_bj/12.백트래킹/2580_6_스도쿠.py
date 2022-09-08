"""
스도쿠는 18세기 스위스 수학자가 만든 '라틴 사각형'이랑 퍼즐에서 유래한 것으로 현재 많은 인기를 누리고 있다.
이 게임은 아래 그림과 같이 가로, 세로 각각 9개씩 총 81개의 작은 칸으로 이루어진 정사각형 판 위에서 이뤄지는데, 
게임 시작 전 일부 칸에는 1부터 9까지의 숫자 중 하나가 쓰여 있다.

나머지 빈 칸을 채우는 방식은 다음과 같다.
1 각각의 가로줄과 세로줄에는 1부터 9까지의 숫자가 한 번씩만 나타나야 한다.
2 굵은 선으로 구분되어 있는 3x3 정사각형 안에도 1부터 9까지의 숫자가 한 번씩만 나타나야 한다.

아홉 줄에 걸쳐 한 줄에 9개씩 게임 시작 전 스도쿠판 각 줄에 쓰여 있는 숫자가 한 칸씩 띄워서 차례로 주어진다. 
스도쿠 판의 빈 칸의 경우에는 0이 주어진다. 스도쿠 판을 규칙대로 채울 수 없는 경우의 입력은 주어지지 않는다.

모든 빈 칸이 채워진 스도쿠 판의 최종 모습을 아홉 줄에 걸쳐 한 줄에 9개씩 한 칸씩 띄워서 출력한다.
스도쿠 판을 채우는 방법이 여럿인 경우는 그 중 하나만을 출력한다.
"""
matrix = [list(map(int, input().split())) for _ in range(9)]
print(matrix)

#0의 개수 : 찾아야할 수의 개수
zeros = []
for i in range(9):
    cnt = matrix[i].count(0)
    zeros.append(cnt)
print(zeros)




# import sys
# import numpy as np
# def fun(x):
#     #for i in range(9):
#         #for j in range(9):
#             #print(matrix[i][j], end="")
#         #print()
#     return
# #0에 들어갈 숫자를 찾으면 True
# z = np.zeros((9,9) ,dtype=bool)
# #입력
# matrix = [list(map(int, input().split())) for _ in range(9)]
# #0의 개수 : 찾아야할 수의 개수
# cnt = 0
# for i in range(9):
#     cnt += matrix[i].count(0)
# fun(0)
