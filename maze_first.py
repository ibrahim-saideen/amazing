import numpy as np
import random
from numpy._typing import NDArray


def left(row: int, col: int, gird: NDArray) -> tuple[int, int] | bool:

    if col-2 > 0 and gird[row][col-2] == 1 and gird[row][col-1] != 8:
        gird[row][col-2] = 0
        gird[row][col-1] = 0
        return ((row, col-2))
    else:
        return False


def right(row: int, col: int, gird: NDArray) -> tuple[int, int] | bool:

    w = (len(gird[0]) - 1) / 2
    if col+2 < w*2 and gird[row][col+2] == 1 and gird[row][col+1] != 8:
        gird[row][col+2] = 0
        gird[row][col+1] = 0
        return ((row, col+2))
    else:
        return False


def up(row: int, col: int, gird: NDArray) -> tuple[int, int] | bool:

    if row-2 > 0 and gird[row-2][col] == 1 and gird[row-1][col] != 8:
        gird[row-2][col] = 0
        gird[row-1][col] = 0
        return ((row-2, col))
    else:
        return False


def down(row: int, col: int, gird: NDArray) -> tuple[int, int] | bool:

    h = (len(gird) - 1) / 2
    if row+2 < h*2 and gird[row+2][col] == 1 and gird[row+1][col] != 8:
        gird[row+2][col] = 0
        gird[row+1][col] = 0
        return ((row+2, col))
    else:
        return False


def creat_maze(h: int, w: int) -> NDArray:
    gird = np.ones((h*2+1, w*2+1))

    a, b = ((h - 5) // 2), (w - 7) // 2

    a = a*2+1
    b = b*2+1

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

    try:
        gird[a: a+9, b:b+13] = pattern

    except ValueError:
        print('Error, cant generate gird smaller than hight = 5 and width = 7')
        exit()

    x, y = (1, 1)

    gird[x, y] = 0
    stack = [(x, y)]
    while (stack):
        a, b = stack[-1]
        directions = [left, right, up, down]
        random.shuffle(directions)
        flag = 1
        for dir in directions:
            result = dir(a, b, gird)
            if result and isinstance(result, tuple):
                flag = 0
                stack.append(result)
                break
        if flag:
            stack.pop()

    return gird
