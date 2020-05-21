N = int(input())

t0, x0, y0 = map(int, input().split())
if t0 < x0 + y0 or t0 % 2 != (x0 + y0) % 2:
    print("No")
    exit()

for i in range(1, N):
    t1, x1, y1 = map(int, input().split())
    dist_t, dist_x, dist_y = abs(t1-t0), abs(x1-x0), abs(y1-y0)
    # print("dist_t: {}, dist_x: {}, dist_y: {}".format(dist_t, dist_x, dist_y))
    if dist_t < dist_x + dist_y or dist_t % 2 != (dist_x + dist_y) % 2:
        print("No")
        exit()
    t0, x0, y0 = t1, x1, y1
print("Yes")
