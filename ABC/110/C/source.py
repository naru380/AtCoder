S = input()
T = input()
N = len(S)

dict_S = {}
dict_T = {}

for i in range(N):
    # print("dict_S: {}".format(dict_S))
    # print("dict_T: {}".format(dict_T))
    if S[i] in dict_S:
        if dict_S[S[i]] != T[i]:
            print("No")
            exit()
    if T[i] in dict_T:
        if dict_T[T[i]] != S[i]:
            print("No")
            exit()
    dict_S[S[i]] = T[i]
    dict_T[T[i]] = S[i]
print("Yes")
