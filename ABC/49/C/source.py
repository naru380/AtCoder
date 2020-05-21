S = input()
S = S[::-1]

DEBUG = False

if DEBUG:
    print("S: {}".format(S))
while True:
    if DEBUG:
        print("S[:7]: {}".format(S[:7]))
    if len(S) >= 5:
        if S[:7] == "remaerd":
            S = S[7:]
        elif S[:6] == "resare":
            S = S[6:]
        elif S[:5] == "maerd" or S[:5] == "esare":
            S = S[5:]
        else:
            print("NO")
            exit()
    else:
        break
if DEBUG:
    print("S: {}".format(S))
if len(S) == 0:
    print("YES")
else:
    print("NO")
