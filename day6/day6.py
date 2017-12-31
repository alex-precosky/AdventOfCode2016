import operator

# keep a list of dicts that track the frequency of letters in each character of a word in the input list

def init_freq_dicts(n):
    freq_dict_list = []

    for i in range(n):
        freq_dict_list.append(dict())

    return freq_dict_list


def insert_into_freq_dicts(word, freq_dicts):
    for i, char in enumerate(word):
        if char in freq_dicts[i]:
            freq_dicts[i][char] += 1
        else:
            freq_dicts[i][char] = 1


if __name__ == "__main__":

    freq_dicts = init_freq_dicts(8)

    for line in open("input.txt", "r").readlines():
        insert_into_freq_dicts(line.strip(), freq_dicts)

    print("Part 1")
    for freq_dict in freq_dicts:
        print(sorted(freq_dict.items(), key=operator.itemgetter(1), reverse=True)[0])

    print("Part 2")
    for freq_dict in freq_dicts:
        print(sorted(freq_dict.items(), key=operator.itemgetter(1), reverse=False)[0])
