from inspect import currentframe

def chkprint(*args):
    names = {id(v):k for k,v in currentframe().f_back.f_locals.items()}
    print(', '.join(names.get(id(arg),'???')+' = '+repr(arg) for arg in args))

def main():
    N, M, V, P = map(int, input().split())
    A = list(map(int, input().split()))
    dic_A = {k:v for (k, v) in enumerate(A)}
    sorted_dic_A = sorted(dic_A.items(), key=lambda x: x[1], reverse=True)
    # chkprint(sorted_dic_A)

    B = sorted_dic_A[:P]
    P_min_val = min(B, key=lambda  x: x[1])[1]
    # chkprint(B)
    C = sorted_dic_A[P:]
    # chkprint(C)

    ans = set()

    num_vote = M * V
    # chkprint(num_vote)
    for i, v in C:
        if P_min_val > v + M:
            break
        margin = num_vote
        margin -= M * (P-1)
        margin_list = [v+M-w for (j,w) in C if j!=i]
        mod_margin_list = list(map(lambda x: x if x < M else M, margin_list))
        # chkprint(margin_list)
        # chkprint(mod_margin_list)
        margin -= M
        margin -= sum(mod_margin_list)
        # chkprint(margin)
        if margin > 0:
            break
        ans.add(i)

    for i, _ in B:
        ans.add(i)

    print(len(ans))


if __name__ == '__main__':
    main()
