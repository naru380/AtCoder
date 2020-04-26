S_dash = input()
T = input()

DEBUG = False

reversed_S_dash = S_dash[::-1]
reversed_T = T[::-1]

for i in range(len(S_dash)-len(T)+1):
    flag = True
    for j in range(len(T)):
        if DEBUG:
            print("i: {}, j: {}".format(i, j))
            print("S_dash[i+j]: {}, T[j]: {}".format(reversed_S_dash[i+j], reversed_T[j]))
        if reversed_S_dash[i+j] != reversed_T[j] and reversed_S_dash[i+j] != '?':
            if DEBUG:
                print("miss match")
            flag = False
            break
    if flag:
        if DEBUG:
            print("find")
            print("from {} to {}".format(i, i+len(T)-1))
        ans = reversed_S_dash[:i]+reversed_T+reversed_S_dash[i+len(T):]
        ans = ans.replace('?', 'a')
        print(ans[::-1])
        exit(0)

print("UNRESTORABLE")
