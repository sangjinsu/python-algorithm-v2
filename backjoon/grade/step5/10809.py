import sys

word = list(sys.stdin.readline().strip())
result = [-1] * (ord('z') - ord('a') + 1)

for idx, letter in enumerate(word):
    asc = ord(letter) - ord('a')
    if result[asc] < 0:
        result[asc] = idx

print(*result)

