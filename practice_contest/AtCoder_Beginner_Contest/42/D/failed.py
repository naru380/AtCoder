from math import factorial as fact

h, w, a, b = list(map(int, input().split()))

x = w-b
y = h-a


p = fact(x + y) // ( fact(x) * fact(y) )

print(p % (10**9 + 7))
