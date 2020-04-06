K = int(input())

flags = [-1] * (10**8+7)

count = 0
now = 1
flags[0] = 1
while count != K:
    if now < 10:
        flags[now] = 1
    elif now < 100:
         if abs((now % 10) - (now // 10)) <= 1:
             flags[now] = 1
         else:
             flags[now] = 0
    else:
        n = int(str(now)[1:])
        if len(str(now)[1:]) != len(str(n)):
            if int(str(n)[0]) == 1 or int(str(n)[0]) == 0:
                if flags[n]:
                    if abs(int(str(now)[0]) - int(str(now)[1])) <= 1:
                        flags[now] = 1
                    else:
                        flags[now] = 0
                else:
                    flags[now] = 0
            else:
                flags[now] = 0
        else:
            if flags[n]:
                if abs(int(str(now)[0]) - int(str(now)[1])) <= 1:
                    flags[now] = 1
                else:
                    flags[now] = 0
            else:
                flags[now] = 0
    if flags[now] == 1:
        count += 1
        # print(now)
    # print('count: {}, now: {}, flag: {}'.format(count, now, flags[now]))
    now += 1

print(now - 1)
