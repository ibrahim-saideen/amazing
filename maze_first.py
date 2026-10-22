import numpy as np
import random

def left(a, b, maze):

    if b-2 > 0 and maze[a][b-2] == 1 and maze[a][b-1] != 8:
         maze[a][b-2] = 0
         maze[a][b-1] = 0
         return((a, b-2))
    else:
         return False

def right(a, b, maze):

    w = (len(maze[0]) - 1) / 2 
    if  b+2 < w*2 and maze[a][b+2] == 1 and maze[a][b+1] != 8:
         maze[a][b+2] = 0
         maze[a][b+1] = 0
         return((a, b+2))
    else:
         return False


def up(a, b, maze):

    if  a-2 > 0 and maze[a-2][b] == 1 and maze[a-1][b] != 8:
         maze[a-2][b] = 0
         maze[a-1][b] = 0
         return((a-2, b))
    else:
         return False

def down(a, b, maze):
    
    h = (len(maze) - 1) / 2
    if  a+2 < h*2 and maze[a+2][b] == 1 and maze[a+1][b] != 8:
         maze[a+2][b] = 0
         maze[a+1][b] = 0
         return((a+2, b))
    else:
         return False
    
def creat_maze(h, w):
     maze = np.ones((h*2+1, w*2+1))
     
     a, b = ((h - 5) // 2), (w - 7) // 2

     a = a*2+1
     b = b*2+1
     pattern = [
          [8,1,1,1,1,1,1,1,8,8,8,8,8],
          [8,1,1,1,1,1,1,1,1,1,1,1,8],
          [8,1,1,1,1,1,1,1,1,1,1,1,8],
          [8,1,1,1,1,1,1,1,1,1,1,1,8],
          [8,8,8,8,8,1,1,1,8,8,8,8,8],
          [1,1,1,1,8,1,1,1,8,1,1,1,1],
          [1,1,1,1,8,1,1,1,8,1,1,1,1],
          [1,1,1,1,8,1,1,1,8,1,1,1,1],
          [1,1,1,1,8,1,1,1,8,8,8,8,8],
          ]

     try:
          maze[a: a+9, b:b+13] = pattern
     except ValueError :
          print('Error : cant generate maze smaller than hight = 5 and width = 7')
          exit()

     
     x, y = (1, 1)
     maze[x, y] = 0
     stack = [(x, y)]
     while(stack):
        a, b = stack[-1]
        directions = [left, right, up, down]
        random.shuffle(directions)
        flage = 1
        for dir in directions:
            result  = dir(a, b, maze)
            if result :
                 flage = 0
                 stack.append(result)
                 break
        if flage:
            stack.pop()
             
     return maze

