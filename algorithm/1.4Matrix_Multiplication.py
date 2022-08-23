"""
행렬의 곱셈 문제
-두 n x m 행렬의 곱을 구하시오
-입력사례 : n = 2
-A = [a11 a12]  B = [b11 b12]
     [a21 a22],     [b21 b22]

-    [2 3] x [5 7] = [28 38]
     [4 1]   [6 8]   [26 36]

- C = A X B, Cij = ai1*b1j + ai2*b2j
"""
def matrixmult(n, A, B):
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C
A = [[2,3], [4,1]]
B = [[5,7], [6,8]]
print('A =', A)
print('B =', B)
C = matrixmult(len(A), A, B)
print('C =', C)