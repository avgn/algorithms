#!/usr/bin/python

# Implementation of the square matrix multiplication algorithm described in CLRS p.75

def square_matrix_multiply(A, B):
    n = len(A)
    C = []
    for i in range(n):
        C.append([])
        for j in range(n):
            C[i].append(0)
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C


def main():
    pass


if __name__ == '__main__':
    main()