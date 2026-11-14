import random
import numpy as np
from numpy.typing import NDArray
from read_config import dic

GridArray = NDArray[np.float64]


def left(row: int, col: int, grid: GridArray) -> tuple[int, int] | None:
    """A function that move a cell to the left neighbour cell in the grid"""
    if col - 2 > 0 and grid[row][col - 2] == 1 and grid[row][col - 1] != 8:
        grid[row][col - 2] = 0
        grid[row][col - 1] = 0
        return (row, col - 2)
    else:
        return None


def right(row: int, col: int, grid: GridArray) -> tuple[int, int] | None:
    """A function that move a cell to the right neighbour cell in the grid"""
    w = (len(grid[0]) - 1) / 2
    if col + 2 < w * 2 and grid[row][col + 2] == 1 and grid[row][col + 1] != 8:
        grid[row][col + 2] = 0
        grid[row][col + 1] = 0
        return (row, col + 2)
    else:
        return None


def up(row: int, col: int, grid: GridArray) -> tuple[int, int] | None:
    """A function that move a cell to the up neighbour cell in the grid"""
    if row - 2 > 0 and grid[row - 2][col] == 1 and grid[row - 1][col] != 8:
        grid[row - 2][col] = 0
        grid[row - 1][col] = 0
        return (row - 2, col)
    else:
        return None


def down(row: int, col: int, grid: GridArray) -> tuple[int, int] | None:
    """A function that move a cell to the down neighbour cell in the grid"""
    h = (len(grid) - 1) / 2
    if row + 2 < h * 2 and grid[row + 2][col] == 1 and grid[row + 1][col] != 8:
        grid[row + 2][col] = 0
        grid[row + 1][col] = 0
        return (row + 2, col)
    else:
        return None


def create_maze(row: int, col: int) -> GridArray:
    # create maze takes the logical coordinates then converts them to
    #  the appropritate shape for the grid, for ex: 3,3 -> 7,7

    grid = np.ones((row * 2 + 1, col * 2 + 1))

    a, b = ((row - 5) // 2), (col - 7) // 2

    # starting points of where the 42 pattern will be inserted
    a = a * 2 + 1
    b = b * 2 + 1

    pattern = [
        [8, 1, 1, 1, 1, 1, 1, 1, 8, 8, 8, 8, 8],
        [8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 8],
        [8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 8],
        [8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 8],
        [8, 8, 8, 8, 8, 1, 1, 1, 8, 8, 8, 8, 8],
        [1, 1, 1, 1, 8, 1, 1, 1, 8, 1, 1, 1, 1],
        [1, 1, 1, 1, 8, 1, 1, 1, 8, 1, 1, 1, 1],
        [1, 1, 1, 1, 8, 1, 1, 1, 8, 1, 1, 1, 1],
        [1, 1, 1, 1, 8, 1, 1, 1, 8, 8, 8, 8, 8],
    ]

    grid[a: a + 9, b: b + 13] = pattern

    y, x = (1, 1)

    grid[y, x] = 0
    stack = [(y, x)]
    if dic['seed'] != None:
        random.seed(dic['seed'])
    while stack:  # not empty
        cur_y, cur_x = stack[-1]
        directions = [left, right, up, down]
        random.shuffle(directions)
        for dir in directions:
            result = dir(cur_y, cur_x, grid)
            if result is not None:
                stack.append(result)
                break
        else:
            stack.pop()
    return grid
