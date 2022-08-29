"""
단어의 순서를 정의하여 정렬하는 문제

알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
1. 길이가 짧은 것부터
2. 길이가 같으면 사전 순으로

첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 
둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 
주어지는 문자열의 길이는 50을 넘지 않는다.

조건에 따라 정렬하여 단어들을 출력한다. 단, 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력한다.
"""
# 람다식을 이상하게 씀
# import sys
# arr = []
# n = int(sys.stdin.readline())
# for _ in range(n):
#     a = sys.stdin.readline().replace('\n','')
#     arr.append([a, len(a)])
# arr.sort(key=lambda x: (x[1], x[0]))
# for i in range(n):
#     del arr[i][1]
# result = []
# for v in arr:
#         if v not in result:
#             result.append(v)
# temp = str(result)
# temp = temp.replace("[","").replace("]","").replace(",","").replace("'","")
# for z in temp.split():
#     sys.stdout.write(z+"\n")

import sys

arr = []
n = int(sys.stdin.readline())
for _ in range(n):
    a = sys.stdin.readline().replace('\n','')
    arr.append(a)
arr = list(set(arr))

arr.sort(key=lambda x: (len(x), x))
for v in arr:
    print(v)