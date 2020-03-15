N = int(input())

def dfs(x, n):
    if len(x) == n:
        s = "".join(chr(ord("a")+x[i]) for i in range(n))
        print(s)
    else:
        # 下桁に近づくにつれて文字の種類が増えるように再帰させる
        for i in range(max(x)+2):
            dfs(x+[i], n)

dfs([0], N)
