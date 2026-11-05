def north(grid, cell):
    x, y = cell
    if grid[x-1][y] == 0:
        return 0
    else:
        return 1
        

def east(grid, cell):
    x, y = cell
    if grid[x][y+1] == 0:
        return 0
    else:
        return 2

def south(grid, cell):
    x, y = cell
    if grid[x+1][y] == 0:
        return 0
    else:
        return 4

def west(grid, cell):
    x, y = cell
    if grid[x][y-1] == 0:
        return 0
    else:
        return 8



def check_directions(grid, cell):

    cell_value = 0
    direction = [north, east, south, west]
    for dir in direction:
        cell_value += dir(grid, cell)
    
    return cell_value


def hexa_maze(grid, output_file):

    with open(output_file, 'w') as file:
    
        for r in range(1, len(grid), 2):
            for c in range(1, len(grid[r]), 2):
                hexa = f'{(check_directions(grid, (r, c))):X}'
                file.write(hexa)
            file.write('\n')
        file.write('\n')

def path_directions(path, start, end, output_file):
    with open(output_file, 'a') as file:
        result = ", ".join(map(str, start))
        file.write(result + '\n')
        result = ", ".join(map(str, end))
        file.write(result + '\n')

        for i in range(len(path) - 1):
            x, y = path[i]
            if (x-2, y) == path[i+1]:
                file.write('N')
            elif (x, y+2) == path[i+1]:
                file.write('E')
            elif (x+2, y) == path[i+1]:
                file.write('S')
            elif (x, y-2) == path[i+1]:
                file.write('W')
        file.write('\n')

