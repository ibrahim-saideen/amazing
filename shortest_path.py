from maze_first import creat_maze
from collections import deque
from read_config import dic, main

def grid_point(maze_point):
     x ,y = maze_point
     x = x*2 + 1
     y = y*2 + 1
     return((x, y))

def left(a, b, maze):

    if b-2 > 0 and maze[a][b-2] == 0 and maze[a][b-1] == 0:
         return((a, b-2))
    else:
         return False

def right(a, b, maze):

    w = (len(maze[0]) - 1) / 2 
    if  b+2 < w*2 and maze[a][b+2] == 0 and maze[a][b+1] == 0:
         return((a, b+2))
    else:
         return False


def up(a, b, maze):

    if  a-2 > 0 and maze[a-2][b] == 0 and maze[a-1][b] == 0:
         return((a-2, b))
    else:
         return False

def down(a, b, maze):

    h = (len(maze) - 1) / 2 
    if  a+2 < h*2 and maze[a+2][b] == 0 and maze[a+1][b] == 0:
         return((a+2, b))
    else:
         return False


def shortest_path(start, end, maze):

     x1, y1 = start
     x2, y2 = end
     x1 = x1*2+1
     y1 = y1*2+1
     x2 = x2*2+1
     y2 = y2*2+1
     end = (x2, y2)

     dq = deque()
     dq.append((x1, y1))

     parents = {}
     parents[(x1, y1)] = None
     directions = [up, right, down, left]
     viseted_cells = []

     while(dq):
          x, y = dq.popleft()
          viseted_cells.append((x,y))
          for dir in directions:
               next_cell = dir(x, y, maze)
               if next_cell and next_cell not in viseted_cells:
                    parents[next_cell] = (x, y)
                    dq.append(next_cell)
                    viseted_cells.append(next_cell)
                    if next_cell == end:
                         break
          if next_cell == end:
               break
     return(parents)

#############################################################################################

main()

height = dic['height']
width = dic['width']
start = dic['entry']
end = dic['exit']

maze = creat_maze(height ,width)

parents = (shortest_path(start, end, maze))

path = []
current = grid_point(end)

while current is not None:
    path.append(current)
    current = parents[current]

path.reverse() 

for item in path:
     x, y = item
     maze[x,y] = 9


for row in maze:
        for cell in row:
            if cell == 0:
                print(" ", end=" ")
            elif cell == 1:
                print("🧱", end="")
            elif cell == 8:
                 print("🟩", end="")
            else:
                 print("⬤",end=" ")
        print()

