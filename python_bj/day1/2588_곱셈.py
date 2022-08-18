#(세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.
#(1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.
#첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다.
#첫째 줄부터 넷째 줄까지 차례대로 (3), (4), (5), (6)에 들어갈 값을 출력한다.

# a = input()
# b = input()
# alist = list(a)
# blist = list(b)
# alist = [int (i) for i in alist]
# blist = [int (i) for i in blist]
# #i, j : 2 ~ 0
# muldic = {}
# result = []
# overflow = 0
# for i in range(2, -1, -1):
#     for j in range(2, -1, -1):
#         mul = blist[i] * alist[j]
#         if mul >= 10:
#             if 'over' in muldic:
#                 overflow = muldic['over']      
#             if j <= 2 and j > 0:
#                 muldic = {'over':mul//10, 'val':((mul + overflow)%10)}
#             else:
#                 muldic = {'over':0, 'val':mul+overflow}
#             #result.insert(0,muldic['val'])
#             result.insert(0, muldic['val'])    
#             result.insert(0, mul)
#         else:
#             print(mul)
#미친짓을 하고 있었음

a = int(input())
b = int(input())

print(a * (b % 10))
print(a * ((b % 100) // 10))
print(a * (b // 100))
print(a * b)


#b를 입력받아 문자열로 슬라이싱
