def first(a, b, c):
    return (a + b) % c


def second(a, b, c):
    return ((a % c) + (b % c)) % c


def third(a, b, c):
    return (a * b) % c


def fourth(a, b, c):
    return ((a % c) * (b % c)) % c


a, b, c = map(int, input().split())

print(first(a, b, c))
print(second(a, b, c))
print(third(a, b, c))
print(fourth(a, b, c))
