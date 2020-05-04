# A^5 - B^5 = (A - B) * (A^4 + A^2*B + AB^2 + B^4)
# X >= 1 なので A > B
# (A^4 + A^2*B + AB^2 + B^4) は 単調増加関数

X = int(input())

a = -1
b = 1
def f(x,y): return x**5-y**5

while f(a, b) != X:
    a += 1
    b = a
    while f(a, b) < X:
        b -= 1
        # print("{}, {}".format(a, b))

print(a, b)
