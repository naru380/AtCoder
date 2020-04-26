S = input()

DEBUG = False

dp = [0] * (len(S)+1)

if int(S[:4]) % 2019 == 0:
    dp[4] += 1

count = 0
for i in range(5,len(S)+1):
    for j in range(i-4+1):
        count += 1
        if DEBUG:
            print("i: {}, j:{}".format(i, j))
            print("string: {}".format(S[i-4-j:i]))
        if int(S[i-4-j:i]) % 2019 == 0:
            if DEBUG:
                print("find!!")
            dp[i] += 1
    # dp[i] += dp[i-1]
    if DEBUG:
        print("dp: {}".format(dp))
if DEBUG:
    print("count: {}".format(count))
    print("dp: {}".format(dp))
# print(dp[len(S)])
print(sum(dp))
