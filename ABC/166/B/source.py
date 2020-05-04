N, K = map(int, input().split())

agent = [False] * (N+1)
agent[0] = True
for _ in range(K):
    _ = input()
    A = list(map(int, input().split()))
    for a in A:
        agent[a] = True

# print(agent)

print(len(list(filter(lambda x: not x, agent))))
