import random
import numpy as np
from numpy._typing import NDArray
from read_config import dic


def left(row: int, col: int, grid: NDArray) -> tuple[int, int] | bool:
    if col - 2 > 0 and grid[row][col - 2] == 1 and grid[row][col - 1] != 8:
        grid[row][col - 2] = 0
        grid[row][col - 1] = 0
        return (row, col - 2)
    else:
        return False


def right(row: int, col: int, grid: NDArray) -> tuple[int, int] | bool:
    w = (len(grid[0]) - 1) / 2
    if col + 2 < w * 2 and grid[row][col + 2] == 1 and grid[row][col + 1] != 8:
        grid[row][col + 2] = 0
        grid[row][col + 1] = 0
        return (row, col + 2)
    else:
        return False


def up(row: int, col: int, grid: NDArray) -> tuple[int, int] | bool:
    if row - 2 > 0 and grid[row - 2][col] == 1 and grid[row - 1][col] != 8:
        grid[row - 2][col] = 0
        grid[row - 1][col] = 0
        return (row - 2, col)
    else:
        return False


def down(row: int, col: int, grid: NDArray) -> tuple[int, int] | bool:
    h = (len(grid) - 1) / 2
    if row + 2 < h * 2 and grid[row + 2][col] == 1 and grid[row + 1][col] != 8:
        grid[row + 2][col] = 0
        grid[row + 1][col] = 0
        return (row + 2, col)
    else:
        return False


def creat_maze(row: int, col: int) -> NDArray:
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

    grid[a : a + 9, b : b + 13] = pattern

    y, x = (1, 1)

    grid[y, x] = 0
    stack = [(y, x)]
    if dic['seed'] != None:
        random.seed(dic['seed'])
    while stack:
        a, b = stack[-1]
        directions = [left, right, up, down]
        random.shuffle(directions)
        flag = 1
        for dir in directions:
            result = dir(a, b, grid)
            if result and isinstance(result, tuple):
                flag = 0
                stack.append(result)
                break
        if flag:
            stack.pop()

    return grid
