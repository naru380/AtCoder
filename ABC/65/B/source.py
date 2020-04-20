N = int(input())
a = [int(input()) for _ in range(N)]

count = 1
now = 1
# print("lightning: {}".format(now))
while count < len(a):
    now = a[now-1]
    # print("lightning: {}".format(now))
    if now == 2:
        print(count)
        exit()
    count += 1

print('-1')
