#두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
#첫째 줄에 테스트 케이스의 개수 T가 주어진다.
#각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
#각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 테스트 케이스 번호는 1부터 시작한다.
list = []
T = int(input())
for i in range(1,T+1):
    a, b = input().split()
    list.append(a)
    list.append(b)

for i in range(0,T*2,2):
    if i == 0:
        case = 1
    else:
        case = case + 1
    print('Case #%d:' % case, int(list[i]) + int(list[i+1]))