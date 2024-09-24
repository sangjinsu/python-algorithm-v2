def solve(a: int, b: int, v: int) -> int:
    day = (v - b) // (a - b)
    if (v - b) % (a - b) > 0:
        day += 1
    return day


if '__main__' == __name__:
    a, b, v = map(int, input().split())
    print(solve(a, b, v))
