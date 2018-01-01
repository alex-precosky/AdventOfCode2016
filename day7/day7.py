import re

def check_four_letters(letters):
    # returns true if the special pattern is present

    if letters[0] == letters[1]:
        return False

    if (letters[0] == letters[3]) and (letters[1] == letters[2]):
        return True

    return False


def check_string(string):
    # looks for the special pattern anywhere in the string

    for i in range(len(string)-3):
        substring = string[i:i+4]
        if check_four_letters(substring) is True:
            return True

    return False


def get_hypernets(address):
    hypernet_regex = "(?<=\[)[a-z]+(?=\])" # matches the hypernets inside of square brackets
    hypernets = re.findall(hypernet_regex, address)

    return hypernets


def get_addresses(address):
    first_address_regex = "[a-z]+(?=\[)" # matches all but the last of the bits
                                         # that are outside square brackets
    last_address_regex = "(?<=\])[a-z]+$" # matches the final instance of that

    first_addresses = re.findall(first_address_regex, address)
    last_address = re.search(last_address_regex, address).group(0)

    addresses = first_addresses.copy()
    addresses.append(last_address)

    return addresses


def get_abbas_for_string(string):
    abbas = []

    for i in range(len(string)-2):
        substring = string[i:i+3]
        if (substring[0] == substring[2]) and (substring[1] != substring[0]):
            abbas.append(substring)

    return abbas


def get_babs_for_abbas(abbas):
    # inverts the abbas into babs, i.e. turns ABA into BAB
    
    babs = []
    for abba in abbas:
        bab = "" + abba[1] + abba[0] + abba[1]
        babs.append(bab)
    return babs


def check_address_SSL(address):
    hypernets = get_hypernets(address)
    supernets = get_addresses(address)

    hypernet_abbas = []
    for hypernet in hypernets:
        hypernet_abbas.extend(get_abbas_for_string(hypernet))
    hypernet_babs = get_babs_for_abbas(hypernet_abbas)

    supernet_abbas = []
    for supernet in supernets:
        supernet_abbas.extend(get_abbas_for_string(supernet))

    for bab in hypernet_babs:
        if bab in supernet_abbas:
            return True

    return False


def check_address_TLS(address):

    hypernets = get_hypernets(address)
    addresses = get_addresses(address)

    for hypernet in hypernets:
        if check_string(hypernet) == True:
            return False

    for subaddress in addresses:
        if check_string(subaddress) == True:
            return True

    return False


if __name__ == "__main__":
    num_supporting_TLS = 0
    for address in open("input.txt", "r").readlines():
        if check_address_TLS(address) is True:
            num_supporting_TLS += 1

    print(f"Part 1: Number of TLS supporting addresses: {num_supporting_TLS}")

    num_supporting_SSL = 0
    for address in open("input.txt", "r").readlines():
        if check_address_SSL(address) is True:
            num_supporting_SSL += 1

    print(f"Part 2: Number of SSL supporting addresses: {num_supporting_SSL}")
# more than 209
