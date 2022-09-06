"""
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다.
중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
수열은 사전 순으로 증가하는 순서로 출력해야 한다.
"""
arr = []
def res():
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(1, n+1):
        if i not in arr:
            arr.append(i)
            res()
            arr.pop()
n, m = map(int, input().split())
res()


# n, m = map(int, input().split())
# arr = []

# def suyeol():
#     if len(arr) == m: #(5) : 리스트의 길이가 수열의 길이 m과 같으면 출력, 아니면 loop
#         print(' '.join(map(str, arr)))
#         return
#     for i in range(1, n+1): #(1) : 1부터 n까지
#         if i not in arr: #(2) : 리스트에 없다면 = 중복되지 않다면 // (6) : 재귀 중이라면 i+1 을 리스트에 추가
#             arr.append(i) #(3) : 추가
#             suyeol() #(4) : 재귀
#             arr.pop() #(6) : 리스트의 길이가 수열의 길이 m과 같다는 조건을 만족하면 출력 후 맨 뒤에 삽입된 i 꺼내고 i 증가
# suyeol()




