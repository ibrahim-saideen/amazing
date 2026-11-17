import subprocess
from perfect import create_maze
from shortest_path import grid_point, shortest_path
from read_config import dic
from gen_output_file import hexa_maze, path_directions
from draw_maze import draw_maze, draw_maze_with_path
from non_perfect import create_non_perfect


def clear_terminal():
    '''
        A terminal cleaner function
    '''
    subprocess.run('clear', check=True)


height = dic['height']
width = dic['width']
start = dic['entry']
end = dic['exit']
output_file = dic['output_file']
perfect = dic['perfect']


if perfect == True:
    maze = create_maze(height, width)
else:
    maze = create_non_perfect(height, width)

a, b = grid_point(start)
c, d = grid_point(end)

try:
    if maze[a][b] == 8 or maze[c][d] == 8:
        raise ValueError('choose a valid point')
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

draw_maze(maze, 0)

show_path = False
color_count = 0
while True:

    print('=== A-Maze-ing ===')
    print('1. Re-generate a new maze')
    print('2. Show/Hide path from entry to exit')
    print('3. rotate maze colors')
    print('4. Quit')
    try:
        choice = input('Choice? (1-4): ')
    except KeyboardInterrupt as e:
        print('\nPlease choose an option (1-4).')
        continue

    if choice == '1':
        clear_terminal()
        color_count = 0
        show_path = False
        if perfect == True:
            maze = create_maze(height, width)
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
        draw_maze(maze, color_count % 3)
    elif choice == '2':
        clear_terminal()
        show_path = not show_path
        if show_path:
            draw_maze_with_path(maze, color_count % 3)
        else:
            draw_maze(maze, color_count % 3)
    elif choice == '3':
        clear_terminal()
        color_count += 1
        if show_path:
            draw_maze_with_path(maze, color_count % 3)
        else:
            draw_maze(maze, color_count % 3)

    elif choice == '4':
        break
    else:
        print('Invalid choice')
