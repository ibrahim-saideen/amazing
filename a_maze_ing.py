from perfect import creat_maze
from shortest_path import grid_point, shortest_path
from read_config import dic, main
from gen_output_file import hexa_maze, path_directions
from draw_maze import draw_maze, draw_maze_with_path
from non_perfect import create_non_perfect

main()

height = dic['height']
width = dic['width']
start = dic['entry']
end = dic['exit']
output_file = dic['output_file']
perfect = dic['perfect']


if perfect == True:
    maze = creat_maze(height, width)
else:
    maze = create_non_perfect(height, width)

a, b = grid_point(start)
c, d = grid_point(end)

try:
    if maze[a][b] == 8 or maze[c][d] == 8:
        raise ValueError('chose a valid point')
except ValueError as e:
    print(e)
    exit()

path = (shortest_path(start, end, maze))
hexa_maze(maze, output_file)
path_directions(path, start, end, output_file)
for item in path[1:-1]:
    x, y = item
    maze[x, y] = 9

x, y = path[0]
maze[x][y] = 7
x, y = path[-1]
maze[x][y] = 7

draw_maze(maze)

count = 0
while True:

    print('=== A-Maze-ing ===')
    print('1. Re-generate a new maze')
    print('2. Show/Hide path from entry to exit')
    print('3. rotate maze colors')
    print('4. Quit')
    choice = input('Choice? (1-4): ')

    if choice == '1':
        if perfect == True:
            maze = creat_maze(height, width)
        else:
            maze = create_non_perfect(height, width)

        path = (shortest_path(start, end, maze))
        hexa_maze(maze, output_file)
        path_directions(path, start, end, output_file)
        for item in path:
            x, y = item
            maze[x, y] = 9
        x, y = path[0]
        maze[x][y] = 7
        x, y = path[-1]
        maze[x][y] = 7
        draw_maze(maze)
    elif choice == '2':
        count += 1
        if count % 2 == 0:
            draw_maze(maze)
        else:
            draw_maze_with_path(maze)
    elif choice == '3':
        ...
    elif choice == '4':
        break
    else:
        print('Invalid choice')
