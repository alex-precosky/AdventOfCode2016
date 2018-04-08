import unittest
from day4 import get_checksum, get_sector_id, get_frequency_dict, check_valid_room


class TestDay4(unittest.TestCase):

    def test_get_checksum(self):
        line = "aaaaa-bbb-z-y-x-123[abxyz]"

        expected = "abxyz"
        actual = get_checksum(line)

        assert expected == actual


    def test_get_sector_id(self):
        line = "aaaaa-bbb-z-y-x-123[abxyz]"

        expected = 123
        actual = get_sector_id(line)
        
        assert expected == actual

            
    def test_get_frequency_dict(self):
        line = "aaaaa-bbb-z-y-x-123[abxyz]"

        expected = {'a': 5, 'b': 3, 'z': 1, 'y' : 1, 'x': 1}

        actual = get_frequency_dict(line)

        assert expected == actual


    def test_valid_room1(self):
        line = "aaaaa-bbb-z-y-x-123[abxyz]"

        expected = True
        actual = check_valid_room(line)

        assert expected == actual


    def test_valid_room2(self):
        line = "a-b-c-d-e-f-g-h-987[abcde]"
            
        expected = True
        actual = check_valid_room(line)

        assert expected == actual


    def test_valid_room3(self):
        line = "not-a-real-room-404[oarel]"

        expected = True
        actual = check_valid_room(line)

        assert expected == actual


    def test_valid_room4(self):
        line = "totally-real-room-200[decoy]"

        expected = False
        actual = check_valid_room(line)

        assert expected == actual
