import sys

while True:
    readline = sys.stdin.readline()
    if readline == '':
        break
    a, b = map(int, readline[:-1].split())
    print(a + b)
