import itertools

N = int(input())
S = input()

r = len(list(filter(lambda x: x == "R", S)))
g = len(list(filter(lambda x: x == "G", S)))
b = len(list(filter(lambda x: x == "B", S)))

# print("r:{}, g:{}, b:{}".format(r, g, b))

ans = r * g * b
RGB = list(itertools.permutations(["R", "G", "B"], 3))

# print(RGB)

for i in range(1, N):
    for j in range(N-i*2):
        if (S[j], S[j+i], S[j+2*i]) in RGB:
            ans -= 1

print(ans)
