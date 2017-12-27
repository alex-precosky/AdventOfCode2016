from enum import Enum, auto


class direction_e(Enum):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()


def get_new_direction(facing, turn):
    # currently facing a compass direction, turning "L" or "R",
    # get the new compass direction
    if facing == direction_e.NORTH:
        if turn == "L":
            return direction_e.WEST
        elif turn == "R":
            return direction_e.EAST
    elif facing == direction_e.SOUTH:
        if turn == "L":
            return direction_e.EAST
        elif turn == "R":
            return direction_e.WEST
    elif facing == direction_e.EAST:
        if turn == "L":
            return direction_e.NORTH
        elif turn == "R":
            return direction_e.SOUTH
    elif facing == direction_e.WEST:
        if turn == "L":
            return direction_e.SOUTH
        elif turn == "R":
            return direction_e.NORTH


def get_position_deltas(facing, num_steps):
    # return (deltaX, deltaY) for the number of steps taking in direction facing

    if facing == direction_e.NORTH:
        return (0, -num_steps)
    elif facing == direction_e.SOUTH:
        return (0, num_steps)
    elif facing == direction_e.EAST:
        return(num_steps, 0)
    elif facing == direction_e.WEST:
        return(-num_steps, 0)


def follow_directions(directions):
    # returns the taxicab distance the Easter Bunny went

    facing = direction_e.NORTH
    posX = 0
    posY = 0

    positions_visited = list()
    positions_visited.append((0, 0))

    found_part2_solution = False

    for direction in directions:
        turn = direction[0]
        num_steps = int(direction[1:])

        facing = get_new_direction(facing, turn)
        deltaX, deltaY = get_position_deltas(facing, num_steps)


        if deltaX != 0:
            signX = int(deltaX/abs(deltaX))
            for i in range(0, deltaX, signX):
                posX += 1*signX
                if (posX, posY) not in positions_visited:
                    positions_visited.append((posX, posY))
                else:
                    if found_part2_solution is False:
                        distance_visited_twice = abs(posX) + abs(posY)
                        print(f"Part 2: distance to a position visited twice: {distance_visited_twice}")
                        found_part2_solution = True

        if deltaY != 0:
            signY = int(deltaY/abs(deltaY))
            for i in range(0, deltaY, signY):
                posY += 1*signY
                if (posX, posY) not in positions_visited:
                    positions_visited.append((posX, posY))
                else:
                    if found_part2_solution is False:
                        distance_visited_twice = abs(posX) + abs(posY)
                        print(f"Part 2: distance to a position visited twice: {distance_visited_twice}")
                        found_part2_solution = True


    return abs(posX) + abs(posY)


if __name__ == "__main__":

    input_line = open("input.txt", "r").readline()

    directions = input_line.split(', ')

    distance = follow_directions(directions)

    print(f"Distance for part 1 is: {distance}")
