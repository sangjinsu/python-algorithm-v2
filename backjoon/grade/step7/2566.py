import sys

mat = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(9)]
max_num, x, y = -1, 0, 0

for i in range(9):
    for j in range(9):
        if max_num < mat[i][j]:
            max_num = mat[i][j]
            x, y = i + 1, j + 1

sys.stdout.write(str(max_num))
sys.stdout.write('\n')
sys.stdout.write(str(x) + ' ' + str(y))
