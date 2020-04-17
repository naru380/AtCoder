import math
import collections

def comb(n, r):
    if n < r:
        return 0
    return math.factorial(n) // (math.factorial(r) * (math.factorial(n - r)))

N = int(input())
A = list(map(int, input().split()))

counter = collections.Counter(A)
dic = {c: comb(counter[c], 2) for c in counter.keys()}
sum_dic = sum(dic.values())

for i in A:
    print(sum_dic - (counter[i] - 1))
