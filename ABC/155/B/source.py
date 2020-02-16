N = int(input())
A = list(map(int, input().split()))
A_odd = list(filter(lambda x: x%2==0, A))

if (len(list(filter(lambda x: (x%3==0)or(x%5==0) ,A_odd))) == len(A_odd)):
    print('APPROVED')
else:
    print('DENIED')
