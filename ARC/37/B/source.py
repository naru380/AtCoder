N, M = map(int, input().split())
m = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(M):
    u, v = map(lambda x: int(x)-1, input().split())
    m[u][v] = 1
    m[v][u] = 1

# print(m)
# for i in range(N):
#     for j in range(N):
#         if m[i][j]:
#             print("i:{}, j:{}".format(i+1, j+1))

vis = [False] * N

def dfs(p, pre_p):
    vis[p] = True
    # print("p:{},pre_p:{}".format(p, pre_p))
    is_tree = True
    for next_p, is_connect in enumerate(m[p]):
        # print("next_p:{}, is_connect:{}".format(next_p, is_connect))
        if pre_p != next_p and is_connect:
            if vis[next_p]:
                is_tree = False
            else:
                is_tree &= dfs(next_p, p) # 1つでも重複で訪れたら木ではない
    return is_tree

ans = 0
for i in range(N):
    if vis[i]:
        continue
    # print("root:{}".format(i))
    if dfs(i, -1):
        ans += 1

print(ans)
