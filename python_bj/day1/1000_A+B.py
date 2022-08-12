#두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
#첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
#첫째 줄에 A+B를 출력한다.

#첫시도 - 입력이 공백이 가운데있는 한 줄이었음 : a b 
#a = int(input())
#b = int(input())
#print(a+b)

a, b = input().split()
print(int(a)+int(b))