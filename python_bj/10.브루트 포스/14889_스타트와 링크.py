"""
첫째 줄에 N(4 ≤ N ≤ 20, N은 짝수)이 주어진다. 
둘째 줄부터 N개의 줄에 S가 주어진다. 각 줄은 N개의 수로 이루어져 있고, 
i번 줄의 j번째 수는 Sij 이다. Sii는 항상 0이고, 
나머지 Sij는 1보다 크거나 같고, 100보다 작거나 같은 정수이다.

첫째 줄에 스타트 팀과 링크 팀의 능력치의 차이의 최솟값을 출력한다.

n/2로 팀을 나누었을 때 두 팀의 능력치 총합끼리의 차이가 가장 적은 경우
백트래킹 : 
스타트 팀의 n/2명이 결정되었을 때 나머지는 링크팀
종료조건 - 현재 탐색이 한 팀의 팀원수(n/2)에 도달했을 때 팀별 능력치 합의 차이를 비교
"""
import sys

n = int(input())
s = list() #능력치 표
# startTeam = 0
# linkTeam = 0
pick = list()
#pick2 = list()
#minVal = 4000001
minVal = list()
for _ in range(n):
    s.append(list(map(int, sys.stdin.readline().split())))

def dfs(arr):
    #print(arr)
    if len(arr) == n/2:                                     #arr의 길이가 n/2개가 되면
        startTeam = 0
        linkTeam = 0
        pick2 = list()
        #global minVal
        #print('arr 길이',len(arr))
        for q in range(n):
            if q not in pick:
                pick2.append(q)
        #print('pick2 길이',len(pick2))

        for j in arr:
            for k in arr:
                if j==k:                                    #자기 자신과 팀인 경우는 없다
                    continue
                startTeam += (s[j][k] + s[k][j])          #스타트팀으로 선별된 사람들의 능력치 합
        for j in pick2:
            for k in pick2:
                if j==k:
                    continue
                linkTeam += (s[j][k] + s[k][j])
        #print('start',startTeam)
        #print('link',linkTeam)
        minVal.append(abs(startTeam-linkTeam))
        #print('min',minVal)
        #print('min',abs(startTeam-linkTeam))
        return
    
    for i in range(len(arr),n):
        #if i not in arr:
            arr.append(i)                                   #0~n까지 순서대로 n/2개 arr에 담기
            dfs(arr)                                        #재귀
            arr.pop()                                      #재귀 나와서 마지막에 들어간 번호 빼고 다음 번호 넣음

dfs(pick)
print(min(minVal))