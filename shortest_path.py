from collections import deque
from numpy.typing import NDArray

import numpy as np
GridArray = NDArray[np.float64]

def grid_point(maze_point: tuple[int, int]) -> tuple[int, int]:
    x, y = maze_point
    x = x * 2 + 1
    y = y * 2 + 1
    return (x, y)


def left(row: int, col: int, grid: GridArray) -> tuple[int, int] | None:

    if col-2 > 0 and grid[row][col-2] == 0 and grid[row][col-1] == 0:
        return ((row, col-2))
    else:
        return None


def right(row: int, col: int, grid: GridArray) -> tuple[int, int] | None:

    w = (len(grid[0]) - 1) / 2
    if col+2 < w*2 and grid[row][col+2] == 0 and grid[row][col+1] == 0:
        return ((row, col+2))
    else:
        return None


def up(row: int, col: int, grid: GridArray) -> tuple[int, int] | None:
    if row-2 > 0 and grid[row-2][col] == 0 and grid[row-1][col] == 0:
        return ((row-2, col))
    else:
        return None


def down(row: int, col: int, grid: GridArray) -> tuple[int, int] | None:

    h = (len(grid) - 1) / 2
    if row+2 < h*2 and grid[row+2][col] == 0 and grid[row+1][col] == 0:
        return ((row+2, col))
    else:
        return None


def shortest_path(
        start: tuple[
        int, int
        ], end: tuple[int, int], grid: GridArray) -> list[tuple[int, int]]:

    start = grid_point(start)
    end = grid_point(end)

    dq: deque[tuple[int, int]] = deque()
    dq.append(start)

    parents: dict[tuple[int, int] , tuple[int, int] | None] = {}
    parents[start] = None
    directions = [up, right, down, left]
    viseted_cells = []

    while (dq):
        x, y = dq.popleft()
        viseted_cells.append((x, y))
        for dir in directions:
            next_cell = dir(x, y, grid)
            if next_cell and next_cell not in viseted_cells:
                parents[next_cell] = (x, y)
                dq.append(next_cell)
                viseted_cells.append(next_cell)
                if next_cell == end:
                    break
            if next_cell == end:
                break
    path = []
    current: tuple[int, int] | None = end

    while current is not None:
        path.append(current)
        current = parents[current]

    path.reverse()
    return path
