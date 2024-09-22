import sys

N, B = map(int, sys.stdin.readline().split())

pivot_chr = 55
result = ''

while N > 0:
    N, m = divmod(N, B)
    result = (str(m) if m < 10 else chr(pivot_chr + m)) + result

sys.stdout.write(result)