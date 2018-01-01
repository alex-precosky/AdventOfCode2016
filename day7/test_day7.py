from day7 import check_four_letters, check_string, get_hypernets, get_addresses


def test_check_four_letters1():
    string = "abba"
    expected = True
    actual = check_four_letters(string)
    assert expected == actual


def test_check_four_letters2():
    string = "mnop"
    expected = False
    actual = check_four_letters(string)
    assert expected == actual


def test_check_four_letters2():
    string = "mnop"
    expected = False
    actual = check_four_letters(string)
    assert expected == actual


def test_check_four_letters3():
    string = "aaaa"
    expected = False
    actual = check_four_letters(string)
    assert expected == actual

def test_check_string1():
    string = "abba"
    expected = True
    actual = check_string(string)
    assert expected == actual


def test_check_string2():
    string = "aaaa"
    expected = False
    actual = check_string(string)
    assert expected == actual


def test_check_string3():
    string = "ioxxoj"
    expected = True
    actual = check_string(string)
    assert expected == actual


def test_check_string4():
    string = "zxcvbn"
    expected = False
    actual = check_string(string)
    assert expected == actual


def test_get_hypernets():
    string = "pcuiwlviqnyoachj[dlgxxylhzwhuvowtr]piyiyrxcvrbtcdn[kcegjaozyiyibnh]uwlkvkmzywsidhgcej[mqgatgmrdlffpjvp]ybsaqisekhdzkgzj"
    expected = ["dlgxxylhzwhuvowtr","kcegjaozyiyibnh", "mqgatgmrdlffpjvp"]

    actual = get_hypernets(string)

    assert expected == actual


def test_get_addresses():
    string = "pcuiwlviqnyoachj[dlgxxylhzwhuvowtr]piyiyrxcvrbtcdn[kcegjaozyiyibnh]uwlkvkmzywsidhgcej[mqgatgmrdlffpjvp]ybsaqisekhdzkgzj"
    expected = ["pcuiwlviqnyoachj", "piyiyrxcvrbtcdn", "uwlkvkmzywsidhgcej", "ybsaqisekhdzkgzj"]

    actual = get_addresses(string)

    assert expected == actual
