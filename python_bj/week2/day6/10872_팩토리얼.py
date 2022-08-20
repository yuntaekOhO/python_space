#0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
#첫째 줄에 정수 N(0 ≤ N ≤ 12)이 주어진다.
#첫째 줄에 N!을 출력한다.

# def factorial(x):
#     if x == 0:
#         return 1
#     return x * factorial(x-1)
# print(factorial(int(input())))


def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n-1)
n = int(input())
print(fac(n))




