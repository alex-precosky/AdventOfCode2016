import hashlib

def is_valid_hash_1(digest):
    if digest[0:5] == "00000":
        return True
    else:
        return False


def is_valid_hash_2(digest, positions):
    position = int(digest[5], base=16)

    if digest[0:5] == "00000" and position < 8 and position not in positions:
        return True
    else:
        return False


if __name__ == "__main__":

    doorID = "wtnhxymk"

    sixth_chars = []
    index = 0
    while len(sixth_chars) < 8:
        if index % 100000 == 0:
            print(index)

        message = doorID + str(index)
        m = hashlib.md5()
        m.update(message.encode('utf-8'))
        digest = m.hexdigest()

        if is_valid_hash_1(digest) is True:
            sixth_char = digest[5]
            sixth_chars.append(sixth_char)
            print(f"Found valid hash at index {index}")

        index += 1

    print(f"Part 1: The password is: {sixth_chars}")

    positions = []
    index = 0
    part_2_password = ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
    while len(positions) < 8:
        if index % 100000 == 0:
            print(index)

        message = doorID + str(index)
        m = hashlib.md5()
        m.update(message.encode('utf-8'))
        digest = m.hexdigest()

        if is_valid_hash_2(digest, positions) is True:
            sixth_char = digest[5]
            seventh_char = digest[6]
            positions.append(int(sixth_char, base=16))
            part_2_password[int(sixth_char)] = seventh_char
            print(positions)
            print(f"Found valid hash at index {index}. Position: {sixth_char}  Value: {seventh_char}  Password: {part_2_password}")

        index += 1


    print(f"Part 2: The password is: {part_2_password}")
