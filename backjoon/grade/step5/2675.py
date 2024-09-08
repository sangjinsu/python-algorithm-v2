import sys

T = int(sys.stdin.readline())
for _ in range(T):
    result = ''
    R, letters = sys.stdin.readline().strip().split()
    times = int(R)
    for letter in letters:
        result += letter * times

    sys.stdout.write(result + '\n')