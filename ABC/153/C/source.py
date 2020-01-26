N, K = map(int, input().split())
H = list(map(int, input().split()))

H_sorted = sorted(H, reverse=True)

print(sum(H_sorted[K:]))
