alphabets = input()
result = 0
if alphabets == ''.join(reversed(alphabets)):
    result = 1

print(result)
