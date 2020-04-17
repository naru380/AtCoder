import math
import copy
import collections

def comb(n, r):
    if n < r:
        return 0
    return math.factorial(n) // (math.factorial(r) * (math.factorial(n - r)))

N = int(input())
A = list(map(int, input().split()))

counter = collections.Counter(A)
dic = {c: comb(counter[c], 2) for c in counter.keys()}

for i in range(N):
    i_comb = comb(counter[A[i]]-1, 2)
    new_dict = copy.deepcopy(dic)
    new_dict[A[i]] = i_comb
    print(sum(new_dict.values()))
