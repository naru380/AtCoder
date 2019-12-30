import copy
import itertools
import heapq

def main():
    N, M, V, P = map(int, input().split())
    A = list(map(int, input().split()))
    ans = set()

    X = [i for i in range(N)]
    Y = [perm for perm in itertools.permutations(X, V)]
    Z = [Y for _ in range(M)]
    #print([perm for perm in itertools.product(*Z)])

    for i in [perm for perm in itertools.product(*Z)]:
        # print(i)
        A_copy = copy.copy(A)
        for j in i:
            for k in j:
                A_copy[k] += 1

        # print(A_copy)
        # psbl = sorted(A_copy, reverse=True)[:P]
        psbl_min = min(heapq.nlargest(P, A_copy))
        psbl_index_list = [i for i, a in enumerate(A_copy) if a >= psbl_min]
        # print(psbl_index_list)
        for l in psbl_index_list:
            ans.add(l)
        # print(ans)

    print(len(ans))

if __name__ == '__main__':
    main()
