from collections import Counter

N = int(input())
S = [input() for _ in range(N)]

counter_S = Counter(S)

max_val = max(counter_S.values())

for k,v in sorted(counter_S.items()):
    if (v == max_val):
        print(k)
