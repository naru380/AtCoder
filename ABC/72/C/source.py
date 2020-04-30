from collections import Counter

N = int(input())
A = [int(i) for i in input().split()]

l = []
for i in A:
	l.extend([i-1, i, i+1])

count = Counter(l)
cand = sorted(count.most_common(), key=lambda x: x[1], reverse=True)[:3]
cand = list(filter(lambda x: cand[2][1]<=x[1], count.most_common()))
ans = 0
for tpl in cand:
    n = len(list(filter(lambda x: x == tpl[0] or x+1 == tpl[0] or x-1 == tpl[0], A)))
    ans = max(ans, n)

print(ans)
