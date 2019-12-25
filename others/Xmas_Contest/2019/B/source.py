import itertools

DEBUG1 = False
DEBUG2 = False
DEBUG3 = True
DEBUG4 = False
DEBUG5 = False

if __name__ == '__main__':
    if DEBUG1:
        X = list(map(int, input().split()))
        S = set()
        D = set()
        for perm in itertools.product(X, repeat=2):
            S.add(perm[0]+perm[1])
            D.add(perm[0]-perm[1])
        print('S:{}\nD:{}'.format(S, D))
        print('S:{} D:{}'.format(len(S), len(D)))
        exit(0)

    if DEBUG2:
        N = int(input())
        for prod in itertools.combinations([i for i in range(1, 30)], r=N):
            S = set()
            D = set()
            #print(prod)
            for perm in itertools.product(prod, repeat=2):
                #print(perm)
                S.add(perm[0]+perm[1])
                D.add(perm[0]-perm[1])
            print('{}'.format(prod))
            if len(S) > len(D):
                #print('{}'.format(prod))
                print('S:{}\nD:{}'.format(S, D))
                exit(0)
        print('end')
        exit(0)

    # N > 14
    if DEBUG3:
        N = int(input())
        ans = [0,2,3,4,5,7]
        for prod in itertools.combinations([i for i in range(8, 30)], r=N):
            S = set()
            D = set()
            list_prod = list(prod)
            list_prod.extend(ans)
            prod = tuple(list_prod)
            #print(prod)
            for perm in itertools.product(prod, repeat=2):
                #print(perm)
                S.add(perm[0]+perm[1])
                D.add(perm[0]-perm[1])
            print('{}'.format(prod))
            if len(S) > len(D):
                #print('{}'.format(prod))
                print('S:{}\nD:{}'.format(S, D))
                exit(0)
        print('end')
        exit(0)

    if DEBUG4:
        N = int(input())
        for prod in itertools.combinations([i for i in range(1, 35)], r=N):
            S = set()
            D = set()
            #print(prod)
            for perm in itertools.product(prod, repeat=2):
                #print(perm)
                S.add(perm[0]+perm[1])
                D.add(perm[0]-perm[1])
            print('{}'.format(prod))
            if len(S)-len(D) == 1:
                #print('{}'.format(prod))
                print('S:{}\nD:{}'.format(S, D))
                exit(0)
        print('end')
        exit(0)

    if DEBUG5:
        N = int(input())
        for n in range(1, N+1):
            print('N:{}'.format(n))
            for prod in itertools.combinations([i for i in range(40)], r=n):
                S = set()
                D = set()
                #print(prod)
                for perm in itertools.product(prod, repeat=2):
                    #print(perm)
                    S.add(perm[0]+perm[1])
                    D.add(perm[0]-perm[1])
                #print('{}'.format(prod))
                #if len(S)-len(D) == 1:
                if len(S) > len(D):
                    print('perm:{}'.format(prod))
                    print('S:{}\nD:{}'.format(S, D))
                    break
        print('end')
        exit(0)


    N, op = input().split()
    N = int(N)

    if N == 1 or N == 2:
        if op  == '=':
            print(' '.join([str(i) for i in range(N)]))
        else:
            print('Merry Christmas!')
    else:
        if op == '=':
            print(' '.join([str(i) for i in range(N)]))
        elif op == '<':
            ans = [str(i) for i in range(N-1)]
            ans.append(str(N))
            print(' '.join(ans))
        else:
            print('Merry Christmas!')
