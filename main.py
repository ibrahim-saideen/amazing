from MazeGen import MazeGenerator

maze_generator = MazeGenerator(
    height=15,
    width=15,
    perfect=False,
    seed=42
)

maze = maze_generator.generate_maze()

path = maze_generator.shortest_path(
    (0, 0),
    (10, 10)
)

print(maze)
print(path)