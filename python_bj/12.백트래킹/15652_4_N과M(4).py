"""
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
조건 1) 1부터 N까지 자연수 중에서 M개를 고른 수열
조건 2) 같은 수를 여러 번 골라도 된다.
조건 3) 고른 수열은 비내림차순이어야 한다.
        - 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다.
중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
수열은 사전 순으로 증가하는 순서로 출력해야 한다.
"""
n, m = map(int, input().split())
arr = []

def suyeol(start):
    if len(arr) == m: 
        print(' '.join(map(str, arr)))
        return
    for i in range(start, n+1):
        arr.append(i) 
        suyeol(i)
        arr.pop()
suyeol(1)
