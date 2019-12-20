from collections import deque

def main():
    R, C = map(int, input().split())
    sx, sy = map(lambda x: int(x)-1, input().split())
    gx, gy = map(lambda x: int(x)-1, input().split())
    maze = [input() for _ in range(R)]

    stack = deque()
    distances = [[-1]*C for _ in range(R)]
    vectors = ((1, 0), (-1, 0), (0, 1), (0, -1))

    distances[sx][sy] = 0
    for vec_x, vec_y in vectors:
        x = sx + vec_x
        y = sy + vec_y
        stack.append((x, y))
        distances[x][y] = float('inf')

    while len(stack):
        x, y = stack.popleft()
        if x < 0 or x >= R or y < 0 or y >= C or maze[x][y] == '#':
            continue
        try:
            for vec_x, vec_y in vectors:
                next_x = x + vec_x
                next_y = y + vec_y
                if distances[next_x][next_y] < 0:
                    stack.append((next_x, next_y))
                    distances[next_x][next_y] = float('inf')
                else:
                    if distances[x][y] > distances[next_x][next_y] + 1:
                        distances[x][y] = distances[next_x][next_y] + 1
        except IndexError:
            pass
        '''
        print('{} {}'.format(x, y))
        for i in range(R):
            print(distances[i])
        '''
        if x == gx and y == gy:
            print(distances[x][y])


if __name__ == '__main__':
    main()
