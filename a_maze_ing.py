from maze_first import creat_maze
from shortest_path import grid_point, shortest_path
from read_config import dic, main

main()

height = dic['height']
width = dic['width']
start = dic['entry']
end = dic['exit']

maze = creat_maze(height, width)

a, b = grid_point(start)
c, d = grid_point(end)

if maze[a][b] == 8 or maze[c][d] == 8:
    print('chose a valid point')
    exit() 



parents = (shortest_path(start, end, maze))

path = []
current = grid_point(end)

while current is not None:
    path.append(current)
    current = parents[current]

path.reverse()

for item in path:
    x, y = item
    maze[x, y] = 9


for row in maze:
    for cell in row:
        if cell == 0:
            print(" ", end=" ")
        elif cell == 1:
            print("🧱", end="")
        elif cell == 8:
            print("🟩", end="")
        else:
            print("⬤", end=" ")
    print()
