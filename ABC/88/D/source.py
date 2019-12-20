import copy
from collections import deque

def main():
    H, W = map(int, input().split())
    maze = [input() for _ in range(H)]

    walled_maze = copy.copy(maze)
    walled_maze[H:H] = [''.join(['#' for _ in range(W+2)])]
    walled_maze[0:0] = [''.join(['#' for _ in range(W+2)])]
    for row_num in range(1, H+1):
        walled_maze[row_num] = '#{}#'.format(walled_maze[row_num])
    # for i in range(H+2):
    #     print(walled_maze[i])

    stack = deque()
    sx, sy = 1, 1
    gx, gy = H, W
    distances = [[-1]*(W+2) for _ in range(H+2)]
    vectors = ((1, 0), (-1, 0), (0, 1), (0, -1))

    distances[sx][sy] = 0
    for vec_x, vec_y in vectors:
        x = sx + vec_x
        y = sy + vec_y
        stack.append((x, y))
        distances[x][y] = float('inf')

    min_path_dist = -1
    while len(stack):
        x, y = stack.popleft()
        if x < 0 or x >= H+1 or y < 0 or y >= W+1 or walled_maze[x][y] == '#':
            continue
        for vec_x, vec_y in vectors:
            try:
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

        # print('{} {}'.format(x, y))
        # print(stack)
        # for i in range(H+2):
        #     print(distances[i])

        if x == gx and y == gy:
            min_path_dist = distances[x][y]
            break

    if min_path_dist < 0:
        print('-1')
    else:
        black_square_num = sum([row.count('#') for row in maze])
        print(H*W-(min_path_dist+1)-black_square_num)

if __name__ == '__main__':
    main()
