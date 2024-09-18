def count_grouping_word(word: str):
    check_start_letter = dict()
    i = 0
    while i < len(word):
        if word[i] not in check_start_letter:
            check_start_letter[word[i]] = i
            i += 1
            continue
        if word[i] in check_start_letter.keys():
            if check_start_letter[word[i]] == i - 1:
                check_start_letter[word[i]] = i
                i += 1
                continue
            else:
                return False

    return True


if __name__ == '__main__':
    N = int(input())
    word_list = [input() for _ in range(N)]
    result = 0
    for word in word_list:
        if count_grouping_word(word):
            result += 1

    print(result)
