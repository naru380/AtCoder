mod = 10**9 + 7
h, w, a, b = list(map(int, input().split()))

t_mod = [1] * (h+w-1) 
for i in range(1, h+w-1):
    t_mod[i] = i * t_mod[i-1] % mod 

t_modinv = list(map(lambda v: pow(v, mod-2, mod), t_mod))

def comb(n, r):
    return t_mod[n] * t_modinv[r] * t_modinv[n-r] % mod

ans = comb(h-a-1+b, b) * comb(a+w-1-b, a) % mod
for i in range(1, w-b):
    ans += (comb(h-a-1+b+i, b+i) - comb(h-a-1+b+i-1, b+i-1)) * comb(a+w-1-b-i, a) % mod

print(ans % mod)
