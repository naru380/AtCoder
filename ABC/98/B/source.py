from collections import Counter

N = int(input())
S = input()
acsum = []

counter = Counter(S)
ans = 0
for i in range(1, N):
    left_counter = Counter(S[:i])
    right_counter = Counter(S[i:])
    left_set = set(left_counter.keys())
    right_set = set(right_counter.keys())
    common_set = left_set & right_set
    ans = max(ans, len(common_set))

print(ans)
