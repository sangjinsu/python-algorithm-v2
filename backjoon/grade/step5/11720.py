import sys

_ = sys.stdin.readline()
num = sys.stdin.readline().strip()
numbers = list(map(int, list(num)))
sys.stdout.write(str(sum(numbers)))
