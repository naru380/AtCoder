from collections import deque

def main():
    H, W = map(int, input().split())
    maze = [input() for _ in range(H)]

    for h in range(H):
        w = maze[h].find('s')
        if w != -1:
            start = (h, w)

    stack = deque()
    explored = [[0]*W for _ in range(H)]

    stack = deque((start, ))
    explored[start[0]][start[1]] = 1
    while len(stack):
        x, y = stack.pop()
        if maze[x][y] == 'g':
            print('Yes')
            exit(0)
        for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            next_x, next_y = x+i, y+j
            if next_x < 0 or next_x >= H or next_y < 0 or next_y >= W:
                continue
            if maze[next_x][next_y] != '#' and (not explored[next_x][next_y]):
                explored[next_x][next_y] = 1
                stack.append((next_x, next_y))
    print('No')


if __name__ == '__main__':
    main()
