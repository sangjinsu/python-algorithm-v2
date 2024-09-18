def alphabet():
    alphabets = input().upper()
    alphabets_dict = dict()

    for letter in alphabets:
        alphabets_dict[letter] = alphabets_dict.get(letter, 0) + 1

    sorted_alphabets = sorted(list(alphabets_dict.items()), key=lambda x: x[1], reverse=True)

    first = sorted_alphabets[0]
    second = ('', 0) if len(sorted_alphabets) <= 1 else sorted_alphabets[1]

    if first[1] == second[1]:
        print('?')
        return
    print(first[0])


if __name__ == '__main__':
    alphabet()
