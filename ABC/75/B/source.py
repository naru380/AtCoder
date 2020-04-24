H, W = map(int, input().split())
maze = []
maze.append('-'*(W+2))
for _ in range(H):
    S = input()
    maze.append('-'+S+'-')
maze.append('-'*(W+2))
# print(maze)

new_maze = [['' for _ in range(W)] for _ in range(H)]
for i in range(1, H+1):
    for j in range(1, W+1):
        if maze[i][j] == '.':
            count = 0
            for k in [-1, 0, 1]:
                for l in [-1, 0, 1]:
                    if k == 0 and l == 0:
                        continue
                    if maze[i+k][j+l] == '#':
                        count += 1
            new_maze[i-1][j-1] = str(count)
        else:
            new_maze[i-1][j-1] = '#'
    print(*new_maze[i-1], sep='')
# print(new_maze)
