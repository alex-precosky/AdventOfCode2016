from itertools import permutations
import re


def check_triangle(sides):
    # return true if the triangle is possible

    for p in permutations(sides):
        if (p[0] + p[1]) <= p[2]:
            return False

    return True
    # sides.sort()
    # if (sides[0] + sides[1]) < sides[2]:
    #     return False
    # else:
    #     return True


def reformat_part_2(sides):
    
    # put all of the sides in one column
    col_1 = []
    col_2 = []
    col_3 = []
    for side in sides:
        col_1.append(side[0])
        col_2.append(side[1])
        col_3.append(side[2])

    col_1.extend(col_2)
    col_1.extend(col_3)

    reformatted_sides = []
    for i in range(0, len(col_1), 3):
        append_list = [col_1[i], col_1[i+1], col_1[i+2]]
        reformatted_sides.append(append_list)

    return reformatted_sides

if __name__ == "__main__":

    num_valid_triangles = 0

    for line in open("input.txt", "r").readlines():
        m = re.findall('\d+', line.strip())
        sides = [int(side) for side in m]
    
        if check_triangle(sides) is True:
            num_valid_triangles += 1

    print(f"Part 1: Number of valid triangles: {num_valid_triangles}")

    # part 2
    sides = []
    for line in open("input.txt", "r").readlines():
        m = re.findall('\d+', line.strip())
        sides.append([int(side) for side in m])

    reformatted_sides = reformat_part_2(sides)

    num_valid_triangles = 0
    for side in reformatted_sides:
        if check_triangle(side) is True:
            num_valid_triangles += 1

    print(f"Part 2: Number of valid triangles: {num_valid_triangles}")
    # more than 1053
