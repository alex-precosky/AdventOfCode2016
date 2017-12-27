def find_next_button_keypad1(starting_button, directions):
    # starting with the finger on a button, and a list of directions,
    # find the button we end up on

    button = starting_button

    for char in directions:
        if button == 1 and char == 'R':
            button = 2
        elif button == 1 and char == 'D':
            button = 4
        elif button == 2 and char == 'L':
            button = 1
        elif button == 2 and char == 'R':
            button = 3
        elif button == 2 and char == 'D':
            button = 5
        elif button == 3 and char == 'L':
            button = 2
        elif button == 3 and char == 'D':
            button = 6
        elif button == 4 and char == 'U':
            button = 1
        elif button == 4 and char == 'R':
            button = 5
        elif button == 4 and char == 'D':
            button = 7
        elif button == 5 and char == 'U':
            button = 2
        elif button == 5 and char == 'L':
            button = 4
        elif button == 5 and char == 'R':
            button = 6
        elif button == 5 and char == 'D':
            button = 8
        elif button == 6 and char == 'U':
            button = 3
        elif button == 6 and char == 'L':
            button = 5
        elif button == 6 and char == 'D':
            button = 9
        elif button == 7 and char == 'U':
            button = 4
        elif button == 7 and char == 'R':
            button = 8
        elif button == 8 and char == 'U':
            button = 5
        elif button == 8 and char == 'L':
            button = 7
        elif button == 8 and char == 'R':
            button = 9
        elif button == 9 and char == 'U':
            button = 6
        elif button == 9 and char == 'L':
            button = 8

    return button


def find_next_button_keypad2(starting_button, directions):
    # starting with the finger on a button, and a list of directions,
    # find the button we end up on

    button = starting_button

    for char in directions:
        if button == 1 and char == 'D':
            button = 3
        elif button == 2 and char == 'R':
            button = 3
        elif button == 2 and char == 'D':
            button = 6
        elif button == 3 and char == 'U':
            button = 1
        elif button == 3 and char == 'L':
            button = 2
        elif button == 3 and char == 'D':
            button = 7
        elif button == 3 and char == 'R':
            button = 4
        elif button == 4 and char == 'L':
            button = 3
        elif button == 4 and char == 'D':
            button = 8
        elif button == 5 and char == 'R':
            button = 6
        elif button == 6 and char == 'U':
            button = 2
        elif button == 6 and char == 'L':
            button = 5
        elif button == 6 and char == 'D':
            button = 'A'
        elif button == 6 and char == 'R':
            button = 7
        elif button == 7 and char == 'U':
            button = 3
        elif button == 7 and char == 'L':
            button = 6
        elif button == 7 and char == 'D':
            button = 'B'
        elif button == 7 and char == 'R':
            button = 8
        elif button == 8 and char == 'U':
            button = 4
        elif button == 8 and char == 'L':
            button = 7
        elif button == 8 and char == 'R':
            button = 9
        elif button == 8 and char == 'D':
            button = 'C'
        elif button == 9 and char == 'L':
            button = 8
        elif button == 'A' and char == 'U':
            button = 6
        elif button == 'A' and char == 'R':
            button = 'B'
        elif button == 'B' and char == 'L':
            button = 'A'
        elif button == 'B' and char == 'U':
            button = 7
        elif button == 'B' and char == 'R':
            button = 'C'
        elif button == 'B' and char == 'D':
            button = 'D'
        elif button == 'C' and char == 'L':
            button = 'B'
        elif button == 'C' and char == 'U':
            button = 8
        elif button == 'D' and char == 'U':
            button = 'B'

    return button


if __name__ == "__main__":

    current_button = 5
    part1_code = []
    for line in open("input.txt", "r"):
        current_button = find_next_button_keypad1(current_button, line)
        part1_code.append(current_button)

    print(f"Part 1 code: {part1_code}")


    current_button = 5
    part2_code = []
    for line in open("input.txt", "r"):
        current_button = find_next_button_keypad2(current_button, line)
        part2_code.append(current_button)

    print(f"Part 2 code: {part2_code}")
