import random
import numpy as np
from numpy.typing import NDArray


def remove_dead_ends(grid: NDArray) -> None:
    rows, cols = grid.shape

    directions = [
        (-2, 0),  # Up
        (2, 0),   # Down
        (0, -2),  # Left
        (0, 2)    # Right
    ]

    changed = True

    while changed:
        changed = False

        for r in range(1, rows - 1, 2):
            for c in range(1, cols - 1, 2):

                if grid[r][c] != 0:
                    continue

                connected = 0
                candidates = []

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    wr, wc = r + dr // 2, c + dc // 2

                    if not (0 < nr < rows - 1 and 0 < nc < cols - 1):
                        continue

                    if grid[nr][nc] == 0 and grid[wr][wc] == 0:
                        connected += 1

                    elif grid[nr][nc] == 0 and grid[wr][wc] == 1:
                        candidates.append((wr, wc))

                if connected == 1 and candidates:
                    wr, wc = random.choice(candidates)
                    grid[wr][wc] = 0
                    changed = True


def add_loops(grid: NDArray, chance: float = 0.1) -> None:
    rows, cols = grid.shape
    #print(grid.shape)
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if (r + c) % 2 == 0 or grid[r][c] != 1:
                continue

            if r % 2 == 1:
                before, after = grid[r][c - 1], grid[r][c + 1]
            else:
                before, after = grid[r - 1][c], grid[r + 1][c]

            if before == 0 and after == 0 and random.random() < chance:
                grid[r][c] = 0


def left(row: int, col: int, grid: NDArray) -> tuple[int, int] | None:
    if col - 2 > 0 and grid[row][col - 2] == 1 and grid[row][col - 1] != 8:
        grid[row][col - 2] = 0
        grid[row][col - 1] = 0
        return (row, col - 2)
    return None


def right(row: int, col: int, grid: NDArray) -> tuple[int, int] | None:
    if col + 2 < len(grid[0]) - 1 and grid[row][col + 2] == 1 and grid[row][col + 1] != 8:
        grid[row][col + 2] = 0
        grid[row][col + 1] = 0
        return (row, col + 2)
    return None


def up(row: int, col: int, grid: NDArray) -> tuple[int, int] | None:
    if row - 2 > 0 and grid[row - 2][col] == 1 and grid[row - 1][col] != 8:
        grid[row - 2][col] = 0
        grid[row - 1][col] = 0
        return (row - 2, col)
    return None


def down(row: int, col: int, grid: NDArray) -> tuple[int, int] | None:
    if row + 2 < len(grid) - 1 and grid[row + 2][col] == 1 and grid[row + 1][col] != 8:
        grid[row + 2][col] = 0
        grid[row + 1][col] = 0
        return (row + 2, col)
    return None


def create_non_perfect(row: int, col: int, loop_chance: float = 0.3) -> NDArray:
    grid = np.ones((row * 2 + 1, col * 2 + 1), dtype=int)

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

    if row >= 5 and col >= 7:
        pa = ((row - 5) // 2) * 2 + 1
        pb = ((col - 7) // 2) * 2 + 1
        grid[pa : pa + 9, pb : pb + 13] = pattern

    grid[1, 1] = 0
    stack = [(1, 1)]
    directions = [left, right, up, down]

    while stack:
        cy, cx = stack[-1]
        random.shuffle(directions)
        for move in directions:
            result = move(cy, cx, grid)
            if result is not None:
                stack.append(result)
                break
        else:
            stack.pop()

    add_loops(grid, loop_chance)
    remove_dead_ends(grid)

    return grid
