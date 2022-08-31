#[재귀 1번]
#0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
#첫째 줄에 정수 N(0 ≤ N ≤ 12)이 주어진다.
#첫째 줄에 N!을 출력한다.

# runtimeError : RecursionError : maximum recursion depth exceeded in comparison
#  n >= 998이면 에러, Python이 정한 최대 재귀 깊이가 더 깊어 졌을 때 발생
# calc(n)을 호출하면 총 n+1번의 재귀 호출이 발생 
# print(calc(n))으로 함수를 호출하고 있기 때문에, print(calc(n))의 재귀의 깊이는 n+2가 됩니다. 
# 따라서, n < 998의 경우에는 RecursionError가 발생하지 않지만, n ≥ 998부터는 RecursionError가 발생하게 됩니다.

# 아래 두 코드 모두 998 이상 입력시 에러, 해결법 : for 사용
# def factorial(x):
#     if x == 0:
#         return 1
#     return x * factorial(x-1)
# print(factorial(int(input())))

# def fac(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fac(n-1)
# n = int(input())
# print(fac(n))
# math.factorial() - 내장 함수있음
def fact(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans
print(fact(int(input())))


