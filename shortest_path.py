from maze_first import creat_maze
from collections import deque
import matplotlib.pyplot as plt

def left(a, b, h, w, maze):

    if b-2 > 0 and maze[a][b-2] == 0 and maze[a][b-1] == 0:
         return((a, b-2))
    else:
         return False

def right(a, b, h, w, maze):

    if  b+2 < w*2 and maze[a][b+2] == 0 and maze[a][b+1] == 0:
         return((a, b+2))
    else:
         return False


def up(a, b, h, w, maze):

    if  a-2 > 0 and maze[a-2][b] == 0 and maze[a-1][b] == 0:
         return((a-2, b))
    else:
         return False

def down(a, b, h, w, maze):
    
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
     end = x2, y2

     dq = deque()
     dq.append((x1, y1))

     parent = {(x1, x2) : None}
     directions = [up, right, down, left]
     viseted = []

     while(dq):
          x, y = dq.popleft()
          viseted.append((x,y))
          for dir in directions:
               next_cell = dir(x, y, 10, 10, maze)
               if next_cell and next_cell not in viseted:
                    parent[(next_cell)] = (x, y)
                    dq.append(next_cell)
                    viseted.append(next_cell)
                    if next_cell == end:
                         break
          if next_cell == end:
               break
     return(parent)

maze = creat_maze(10,20)

parents = (shortest_path((0,0),(8,8),maze))

for point in parents:
     x, y= point
     maze[x][y] = 9


plt.figure(figsize=(50, 50))
plt.imshow(maze, cmap="binary")  # 'binary' turns 0 to white and 1 to black
plt.xticks([])  # Remove x-axis tick marks
plt.yticks([])  # Remove y-axis tick marks
plt.title("Maze Visualization")
plt.savefig('MaenIbrahim.PNG')
          


      
