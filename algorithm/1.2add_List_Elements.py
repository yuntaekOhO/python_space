"""
리스트 원소의 합 구하기
문제 : n개의 원소를 가진 리스트 S의 원소의 합을 구하시오
해답 : 리스트 S의 모든 원소들의 합
파라미터 : 리스트 S, 정수 n
입력사례 : S = [-1,10,7,11,5,13,8], n = 6 ; 0번 인덱스는 허수
출력사례 : sum = 54
알고리즘 : S의 모든 원소를 차례대로 sum에 더하는 절차
-sum을 0으로 초기화
-모든 S의 원소에 대해서 sum += S[i]를 실행
-sum의 값을 리턴
"""
def sum(n, S):
    result = 0
    for i in range(1, n+1):
        result = result + S[i]
    return result
S = [-1,10,7,11,5,13,8]
sum = sum(len(S)-1, S)
print("sum =", sum)

def sum(n, S):
    result = 0
    for i in range(1, n):
        result += S[i]
    return result
S = [-1,10,7,11,5,13,8]
sum = sum(len(S), S)
print("sum =", sum)