S = input()
T = input()

if len(S) < len(T):
    # print(S[:-1])
    if T[:-1] == S:
        print("Yes")
    else:
        print("No")
else:
    print("No")
