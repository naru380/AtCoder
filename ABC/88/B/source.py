N = int(input())
A = [int(i) for i in input().split()]
A.sort(reverse=True)

if N == 1:
	print(A[0])
else:
	Alice = sum(A[0::2])
	Bob = sum(A[1::2])
	print(Alice-Bob)
