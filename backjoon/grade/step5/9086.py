import sys

T = int(sys.stdin.readline())
for _ in range(T):
    S = sys.stdin.readline().strip()
    sys.stdout.write(S[0] + S[-1] + '\n')