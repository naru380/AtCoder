from collections import Counter

MOD = 998244353

N = int(input())
D = [int(i) for i in input().split()]

counter = Counter(D)
# print("counter: {}".format(counter))

if D[0] != 0:
    ans = 0
else:
    ans = 1
    count = 1
    for i, item in enumerate(sorted(counter.items(), key=lambda x: x[0])):
        # print("ans: {}".format(ans))
        # print("i: {}, item: {}".format(i, item))
        if i != item[0]:
            ans = 0
            break
        if item[0] == 0 and item[1] != 1:
            ans = 0
            break

        ans *= (count ** item[1]) % MOD
        count = item[1]
print(ans % MOD)
