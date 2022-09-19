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
s = []
startTeam = []
linkTeam = []
minVal = 4000001
for _ in range(n):
    s.append(list(map(int, sys.stdin.readline().split())))

def matching(index1):
    if index1 == n/2:
        for i in range(index1):
            startSum += s[i]
            linkSum += s[i]
    
    for i in range(n):
        for j in range(n):
            if i == j : pass
            startTeam.append()