import copy
from collections import deque

def dfs(island, start, o_num):
    stack = deque()
    explored = [[0]*10 for _ in range(10)]

    stack = deque((start, ))
    explored[start[0]][start[1]] = 1
    n = 0
    while len(stack):
        x, y = stack.pop()
        if island[x][y] == 'o':
            n += 1
        if o_num == n:
            return True
        for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            next_x, next_y = x+i, y+j
            if next_x < 0 or next_x >= 10 or next_y < 0 or next_y >= 10:
                continue
            if island[next_x][next_y] != 'x' and (not explored[next_x][next_y]):
                explored[next_x][next_y] = 1
                stack.append((next_x, next_y))
    return False

def main():
    island = [input() for _ in range(10)]

    for i in range(10):
        for j in range(10):
            copy_island = copy.copy(island)
            copy_island[i] = copy_island[i][:j] + 'o' + copy_island[i][j+1:]
            o_num = ''.join(copy_island).count('o')
            start = (i, j)
            if dfs(copy_island, start, o_num):
                print('YES')
                exit(0)
    print('NO')


if __name__ == '__main__':
    main()
