import random
import numpy as np
from numpy.typing import NDArray

from collections import deque

GridArray = NDArray[np.float64]


class MazeGeneartor:
    def __init__(self, height, width, perfect=False):

        try:
            if height < 7:
                    raise ValueError ('Error, height must be greater than or equal to 7')
            if width < 9:
                    raise ValueError ('Error, width must be greater than or equal to 9')
            
            self.height = height
            self.width = width
            self.perfect = perfect
        except ValueError as e:
            print(e)
            exit(1)
        
        
    def generate_maze(self):

        
        def remove_dead_ends(grid: GridArray) -> None:
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


        def add_loops(grid: GridArray, chance: float = 0.1) -> None:
            rows, cols = grid.shape
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


        def left(row: int, col: int, grid: GridArray) -> tuple[int, int] | None:
            if col - 2 > 0 and grid[row][col - 2] == 1 and grid[row][col - 1] != 8:
                grid[row][col - 2] = 0
                grid[row][col - 1] = 0
                return (row, col - 2)
            return None


        def right(row: int, col: int, grid: GridArray) -> tuple[int, int] | None:
            if col + 2 < len(grid[0]) - 1 and grid[
                    row][col + 2] == 1 and grid[row][col + 1] != 8:
                grid[row][col + 2] = 0
                grid[row][col + 1] = 0
                return (row, col + 2)
            return None


        def up(row: int, col: int, grid: GridArray) -> tuple[int, int] | None:
            if row - 2 > 0 and grid[
                    row - 2][col] == 1 and grid[row - 1][col] != 8:
                grid[row - 2][col] = 0
                grid[row - 1][col] = 0
                return (row - 2, col)
            return None


        def down(row: int, col: int, grid: GridArray) -> tuple[int, int] | None:
            if row + 2 < len(grid) - 1 and grid[
                    row + 2][col] == 1 and grid[row + 1][col] != 8:
                grid[row + 2][col] = 0
                grid[row + 1][col] = 0
                return (row + 2, col)
            return None


        
        row = self.height
        col = self.width
        perfect = self.perfect
            
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
            grid[pa: pa + 9, pb: pb + 13] = pattern

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

        if not perfect:
            add_loops(grid, 0.3)
            remove_dead_ends(grid)

        self.grid = grid

        return grid

    def shortest_path(self,
        start: tuple[
        int, int
        ], end: tuple[int, int]) -> list[tuple[int, int]]:


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


        start = grid_point(start)
        end = grid_point(end)

        dq: deque[tuple[int, int]] = deque()
        dq.append(start)

        parents: dict[tuple[int, int], tuple[int, int] | None] = {}
        parents[start] = None
        directions = [up, right, down, left]
        viseted_cells = []

        while (dq):
            x, y = dq.popleft()
            viseted_cells.append((x, y))
            for dir in directions:
                next_cell = dir(x, y, self.grid)
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
