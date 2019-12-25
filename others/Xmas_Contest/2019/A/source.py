PATH = './signboard_t1/pieces/'


if __name__ == '__main__':
    ans = [
        [12, 62, 3, 38, 35, 59, 1, 13],
        [46, 47, 14, 61, 11, 4, 43, 2],
        [53, 30, 9, 10, 42, 26, 27, 15],
        [18, 54, 17, 44, 49, 28, 32, 19],
        [36, 21, 33, 22, 7, 8, 50, 40],
        [34, 41, 25, 52, 60, 63, 20, 29],
        [45, 56, 57, 31, 58, 23, 6, 39],
        [51, 48, 55, 16, 64, 24, 5, 37]
    ]
    for i in range(8):
        row = []
        for _ in range(32):
            row.append('')
        #print(row)
        for j in ans[i]:
            #print('{} {}'.format(i, j))
            f = open(PATH + str(j) + '.txt')
            lines = f.readlines()
            for k in range(32):
                #lines[k].rstrip('\n')
                row[k] = row[k] + lines[k][:-1]
                #print(row[k])
                #print(len(row[k]))
        for line in row:
            print(line)
