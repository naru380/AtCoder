N = int(input())
K = int(input())
X = list(map(int, input().split()))
ans = 0
for x in X:
    # print("x: {}, abs(x-K): {}".format(x, abs(x-K)))
    ans += 2 * min(abs(x-K), x)

print(ans)
