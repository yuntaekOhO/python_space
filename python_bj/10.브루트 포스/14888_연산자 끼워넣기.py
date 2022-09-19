"""
입력 :
n개의 수열 첫번째 입력
수열의 값 두번째 입력
연산자 별 개수 (+, -, *, /)
출력 :
첫째 줄에 만들 수 있는 식의 결과의 최댓값
둘째 줄에 최소값을 출력

숫자의 순서 변경 불가능, 연산자만 변경 가능
모든 경우의 수 해보기
"""
n = int(input())
nums = list(map(int, input().split()))
oper = list(map(int, input().split()))

#덧셈 뺄셈 곱셈 나눗셈 함수를 만들어 놓고 연산하려고 했는데
#이러면 연산자의 위치를 바꿔보면서 값을 찾을 수 없었다
# def plus(oper, a, b):
#     if oper[0] == 0: return
#     oper[0] -= 1
#     return a + b
# def minus(oper, a, b):
#     if oper[1] == 0: return
#     oper[1] -= 1
#     return a - b
# def mul(oper, a, b):
#     if oper[2] == 0: return
#     oper[2] -= 1
#     return a * b
# def div(oper, a, b):
#     if oper[3] == 0: return
#     oper[3] -= 1
#     if a < 0: return -(abs(a) // b)
#     return a // b

#백트래킹
#최초 재귀함수 입력값 : 1, nums[0] - 1=몇번째 수열인지 확인, nums[0]=해당위치의 수열값 ==> 재귀를 하며 다음값으로 변함
#최댓값, 최소값 -10억, 10억으로 초기화
maxVal = -1e9
minVal = 1e9
def dfs(i, arr):
    #전역변수로 사용 : 지역변수일 경우 매 재귀에서 값이 초기화 되버림
    global nums, oper, maxVal, minVal
    
    if i == n:#재귀 종료 조건 : 특정 순서의 연산자로 계산을 마친 경우 1+2+3*4-5
        maxVal = max(maxVal, arr)
        minVal = min(minVal, arr)
    else:
        #연산자들 중 +을 먼저 배치시켜 계산해보고 최대,최솟값으로 지정 + > - > * > /
        #함수스택에서 빠지며(가장 뒤에있는 연산자 먼저 다른 연산자로 바꾸며 모든 경우 계산) 최대,최솟값 비교
        #덧셈
        if oper[0] > 0:
            oper[0] -= 1
            dfs(i+1, arr + nums[i])
            oper[0] += 1
        #뺄셈 1+2+3-4*5
        if oper[1] > 0:
            oper[1] -= 1
            dfs(i+1, arr - nums[i])
            oper[1] += 1
        #곱셈
        if oper[2] > 0:
            oper[2] -= 1
            dfs(i+1, arr * nums[i])
            oper[2] += 1
        #나눗셈
        if oper[3] > 0:
            oper[3] -= 1
            if arr < 0:
                dfs(i+1, -(abs(arr) // nums[i]))
            else:
                dfs(i+1, arr // nums[i])
            oper[3] += 1
dfs(1, nums[0])
print(maxVal)
print(minVal)