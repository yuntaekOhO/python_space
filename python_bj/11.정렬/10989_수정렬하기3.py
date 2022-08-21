#N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
#첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.
#첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

#메모리 초과
# t = int(input())
# num = []

# for _ in range(t):
#     num.append(int(input()))  # for문 속에서 append 사용하면 메모리 재할당의 이유로 메모리 비효율적

# sortNum = sorted(num)

# for i in num:
#     print(i)

#sys.stdin.readline() : input()보다 빠름
#입력 가능한 수의 갯수는 10,000,000개지만 입력 가능한 수의 범위는 10000개이다
#중복이 허용됨
#이럴 때 사용할 수 있는 정렬법인 계수정렬
#반복문을 통해 i를 여러줄에 입력된 수의 값을 알아내고
#j for문에서 실제로 배열에 저장된 데이터는 중복된 수의 개수인 점을 이용
#시간초과 : sys.stdin.readline() 사용
#메모리초과 : sort(), append()등을 loop내에서 사용하지 않음
import sys
t = int(sys.stdin.readline())
numList = [0] * 10001

for _ in range(t):
    numList[int(sys.stdin.readline())] += 1
for i in range(10001):
    if numList[i] != 0:
        for j in range(numList[i]):
            print(i)

