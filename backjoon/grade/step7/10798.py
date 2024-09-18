import sys

row = 5
letter_list = [sys.stdin.readline().strip() for _ in range(row)]
max_column_length = max(map(len, letter_list))

result = ''
for x in range(max_column_length):
    for y in range(row):
        if len(letter_list[y]) <= x:
            continue
        result += letter_list[y][x]

sys.stdout.write(result)
