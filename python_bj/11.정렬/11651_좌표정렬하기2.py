"""
좌표를 다른 순서로 정렬하는 문제
2차원 평면 위의 점 N개가 주어진다. 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다.
(-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.

첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.
"""
# [교환 정렬]
# import sys
# n = int(sys.stdin.readline())
# nums = []
# for _ in range(n):
#     nums.append(list(map(int, sys.stdin.readline().split())))
# for j in range(n):
#     for k in range(n-1):
#         if nums[k][1] > nums[k+1][1]:
#             nums[k], nums[k+1] = nums[k+1], nums[k]
#         elif nums[k][1] == nums[k+1][1]:
#             if nums[k][0] > nums[k+1][0]:
#                 nums[k], nums[k+1] = nums[k+1], nums[k]
# print(nums)

import sys
n = int(sys.stdin.readline())
nums = []
for _ in range(n):
    nums.append(list(map(int, sys.stdin.readline().split())))
nums.sort(key=lambda x: (x[1], x[0])) # 람다식

for i in nums:
    result = str(i[0])+' '+str(i[1])
    print(result)


"""
sort(key=?) = key(속성)=?(함수) : 함수의 결과에 따라 정렬 조건(기준)을 정함 x[0],x[1], x[0],x[1], x[0],x[1], x[0],x[1]
lambda : 함수를 간단히 표현, x = 함수의 인자, (x[1], x[0]) = 리스트  [ [a, b],    [c, d],    [e, f],   [g, h] ]
: 리스트의 1번 인덱스를 비교해 오름차순 정렬을 하고 만약 1번 인덱스끼리의 순서가 같다면 0번 인덱스로 정렬함
"""
