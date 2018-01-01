import numpy as np
import matplotlib.pyplot as plt


def init_grid(width, height):
    return np.zeros((height, width), dtype=bool)


def add_rect(grid, width, height):
    for i in range(width):
        for j in range(height):
            grid[j, i] = True

    return grid


def do_rotate_row(grid, index, amount):
    grid[index] = np.roll(grid[index], amount)
    return grid


def do_rotate_column(grid, index, amount):
    grid[:, index] = np.roll(grid[:, index], amount)
    return grid


def process_line(grid, line):
    tokens = line.split(' ')
    if tokens[0] == "rect":
        width = int(tokens[1].split('x')[0])
        height = int(tokens[1].split('x')[1])
        grid = add_rect(grid, width, height)
    elif tokens[0] == "rotate":
        index = int(tokens[2].split('=')[1])
        amount = int(tokens[4])
        if tokens[1] == "row":
            grid = do_rotate_row(grid, index, amount)
        elif tokens[1] == "column":
            grid = do_rotate_column(grid, index, amount)

    return grid


if __name__ == "__main__":
    grid = init_grid(width=50, height=6)

    for line in open("input.txt", "r").readlines():
        grid = process_line(grid, line)

    num_on_pixels = sum(sum(grid))
    print(f"Part 1: {num_on_pixels} pixels are on")

    # for part two, visualize the grid and read the code off the plot
    plt.imshow(grid)
    plt.show()
