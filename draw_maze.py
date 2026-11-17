from numpy.typing import NDArray
import numpy as np
GridArray = NDArray[np.float64]


def draw_maze(maze: GridArray, color: int) -> None:
    for row in maze:
        for cell in row:
            if cell == 0 or cell == 9:
                print(" ", end=" ")
            elif cell == 7:
                print("🔴", end="")
            elif cell == 1:
                if color == 0:
                    print("🧱", end="")
                elif color == 1:
                    print("🟦", end="")
                elif color == 2:
                    print("🟪", end="")
            elif cell == 8:
                print("🟩", end="")
        print()


def draw_maze_with_path(maze: GridArray, color: int) -> None:
    for row in maze:
        for cell in row:
            if cell == 0:
                print(" ", end=" ")
            elif cell == 7:
                print("🔴", end="")
            elif cell == 1:
                if color == 0:
                    print("🧱", end="")
                elif color == 1:
                    print("🟦", end="")
                elif color == 2:
                    print("🟪", end="")
            elif cell == 8:
                print("🟩", end="")
            else:
                print("⦁︎", end=" ")
        print()
