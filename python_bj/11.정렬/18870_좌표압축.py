"""
만약 정확한 값이 필요 없고 값의 대소 관계만 필요하다면, 모든 수를 0 이상 N 미만의 수로 바꿀 수 있습니다.

수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.
Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.
X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.

첫째 줄에 N이 주어진다.
둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.

첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력한다.
이해 : 나열된 수 차례대로 자기보다 작은 수의 개수 출력
"""
# import sys
# n = int(sys.stdin.readline())
# nums = sys.stdin.readline().split()
# cnts = [0] * n
# for i in range(n):
#     for j in range(n):
#         if int(nums[i]) > int(nums[j]):
#             cnts[i] += 1

# print(cnts)

import sys
N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
#arr2 = []
arr2 = list(sorted(set(arr)))
dic = {arr2[i]:i for i in range (len(arr2))}
for i in arr:
  print(dic[i],end=' ')