def count_croatia_alphabet():
    croatia_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

    alphabets = input()

    i = len(alphabets) - 1
    count = 0
    while i >= 0:
        if alphabets[i] in ['=', '-', 'j']:
            if alphabets[i - 2:i + 1] == 'dz=':
                i -= 3
                count += 1
                continue
            if alphabets[i - 1:i + 1] in croatia_alphabet:
                i -= 2
                count += 1
                continue
        i -= 1
        count += 1

    print(count)


if __name__ == '__main__':
    count_croatia_alphabet()
