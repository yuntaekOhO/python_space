"""
첫째 줄에 N(4 ≤ N ≤ 20, N은 짝수)이 주어진다. 
둘째 줄부터 N개의 줄에 S가 주어진다. 각 줄은 N개의 수로 이루어져 있고, 
i번 줄의 j번째 수는 Sij 이다. Sii는 항상 0이고, 
나머지 Sij는 1보다 크거나 같고, 100보다 작거나 같은 정수이다.

첫째 줄에 스타트 팀과 링크 팀의 능력치의 차이의 최솟값을 출력한다.

1.능력치 표를 s에 저장
2.재귀함수에 빈 배열(pick)을 인자로 실행, 함수 내에선 arr
3.arr에 len(arr) ~ n 까지의 값을 넣고 재귀
4.그러다 len(arr)이 n/2가 되면 arr에 없는 len(arr) ~ n 까지의 값을 pick2에 넣고
* arr(pick) = 스타트 팀, pick2 = 링크 팀
5.능력치표 s의 인덱스로써 arr과 pick2 사용
6.arr의 요소를 사용한 값의 합과 pick2의 요소를 사용한 값의합의 차를 구해 minVal에 저장
7.재귀를 통해 모든 경우의 차를 모두 구하고
8.재귀가 끝나면 minVal의 최소값을 출력

n/2로 팀을 나누었을 때 두 팀의 능력치 총합끼리의 차이가 가장 적은 경우
백트래킹 : 
스타트 팀의 n/2명이 결정되었을 때 나머지는 링크팀
종료조건 - 현재 탐색이 한 팀의 팀원수(n/2)에 도달했을 때 팀별 능력치 합의 차이를 비교
"""
#[시간초과!!]
import sys

n = int(sys.stdin.readline())
s = list() #능력치 표
pick = list()

minVal = list()
for _ in range(n):
    s.append(list(map(int, sys.stdin.readline().split())))

def dfs(arr):
    if len(arr) == n/2:                                     #재귀 종료 조건 : arr의 길이가 n/2개가 되면
        startTeam = 0
        linkTeam = 0
        pick2 = list()

        for q in range(n):                                  #arr에 들어있는 번호 = 스타트팀 번호
            if q not in arr:                                #arr에 not in한 번호 = 링크팀 번호
                pick2.append(q)

        for j in arr:
            for k in arr:
                if j==k:                                    #자기 자신과 팀인 경우는 없다
                    continue
                startTeam += (s[j][k])          #스타트팀으로 선별된 사람들의 능력치 합, 2중 for문으로 (j,k)+(k,j) 안해도 됨
        for j in pick2:
            for k in pick2:
                if j==k:
                    continue
                linkTeam += (s[j][k])
        minVal.append(abs(startTeam-linkTeam)) #두 팀의 차이를 minVal 리스트에 저장
        return
    
    #종료조건에 만족하기 전
    for i in range(len(arr),n):
        arr.append(i)                                   #0~n까지 순서대로 n/2개 arr에 담기
        dfs(arr)                                        #재귀
        arr.pop()                                      #재귀 나와서 마지막에 들어간 번호 빼고 다음 번호 넣음

dfs(pick)                                               #pick은 list()로 선언만 해둔 상태
print(min(minVal))