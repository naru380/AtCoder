a, b, x = map(int, input().split())
b_mod = b//x+1
a_mod = (a-1)//x+1 if a > 0 else 0
ans = b_mod - a_mod
print(ans)
