import operator


def get_checksum(line):
    after_bracket = line.split('[')[1]
    return after_bracket.split(']')[0]


def get_sector_id(line):
    before_bracket = line.split('[')[0]
    return int(before_bracket.split('-')[-1])


def get_frequency_dict(line):
    before_bracket = line.split('[')[0]
    digest = "".join(before_bracket.split('-')[0:-1])

    frequency_dict = dict()

    for char in digest:
        if char not in frequency_dict:
            frequency_dict[char] = 1
        else:
            frequency_dict[char] += 1

    return frequency_dict


def check_valid_room(line):
    checksum = get_checksum(line)

    frequency_dict = get_frequency_dict(line)

    calculated_checksum = "".join(list(zip(*sorted(sorted(frequency_dict.items(), key=operator.itemgetter(0)), key=operator.itemgetter(1), reverse=True)))[0][0:5])

    if calculated_checksum == checksum:
        return True
    else:
        return False


def cycle_char(char, n):
    return chr((((ord(char) - ord('a')) + n) % 26) + ord('a'))


def cycle_string(in_str, n):
    return_str = ""

    for char in in_str:
        cycled_char = cycle_char(char, n)
        return_str += str(cycled_char)

    return return_str


if __name__ == "__main__":

    sum_of_valid_room_sector_ids = 0

    for line in open("input.txt", "r").readlines():
        if check_valid_room(line.strip()) is True:
            sector_id = get_sector_id(line)
            sum_of_valid_room_sector_ids += sector_id
            decrypted_name = cycle_string(line, sector_id)
            print(f"{decrypted_name} sector id: {sector_id}")

    print("Part 1: Sum of sector IDs of valid rooms: "
          f"{sum_of_valid_room_sector_ids}")
