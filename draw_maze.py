def draw_maze(maze):
    for row in maze:
        for cell in row:
            if cell == 0 or cell == 9:
                print(" ", end=" ")
            elif cell == 7:
                print("🔴", end="")
            elif cell == 1:
                print("🧱", end="")
            elif cell == 8:
                print("🟩", end="")
        print()


def draw_maze_with_path(maze):
     for row in maze:
        for cell in row:
            if cell == 0:
                print(" ", end=" ")
            elif cell == 7:
                print("🔴", end="")
            elif cell == 1:
                print("🧱", end="")
            elif cell == 8:
                print("🟩", end="")
            else:
                print("⬤", end=" ")
        print()
