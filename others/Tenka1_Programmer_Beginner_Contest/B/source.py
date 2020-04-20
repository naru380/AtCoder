N = int(input())
A, B = map(int, input().split())
for _ in range(N-1):
    A_n, B_n = map(int, input().split())
    if A_n > A:
        A = A_n
        B = B_n

print(A+B)
