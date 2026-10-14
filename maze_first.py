import numpy as np
import random
import matplotlib.pyplot as plt

def left(a, b, h, w, maze):
    if (b-2 < 0):
        return False
    elif (maze[a][b-2] == 0):
                return False
    elif (maze[a][b-2] == 8):
                    return False
    else:
        maze[a][b-2] = 0
        if maze[a][b-1] == 1:
            maze[a][b-1] = 0
        return((a, b-2))

def right(a, b, h, w, maze):
    if(b+2 > w*2):
        return False
    elif(maze[a][b+2] == 0):
         return False
    elif(maze[a][b+2] == 8):
             return False

    else:
        maze[a][b+2] = 0
        if maze[a][b+1] == 1:
            maze[a][b+1] = 0
        return((a, b+2))


def up(a, b, h, w, maze):
    if (a-2 < 0):
            return False
    elif (maze[a-2][b] == 0):
         return False
    elif (maze[a-2][b] == 8):
        return False

    else:
        maze[a-2][b] = 0
        if maze[a-1][b] == 1:
            maze[a-1][b] = 0
        return((a-2, b))

def down(a, b, h, w, maze):
    if(a+2 > h*2):
            return False
    elif(maze[a+2][b] == 0):
         return False
    elif(maze[a+2][b] == 8):
             return False
        
    else:
        maze[a+2][b] = 0
        if maze[a+1][b] == 1:
            maze[a+1][b] = 0
        return((a+2, b))

def creat_maze(h, w):
    maze = np.ones((h*2+1, w*2+1))

    a, b = ((h - 5) // 2), (w - 7) // 2

    a = a*2+1
    b = b*2+1
    pattern = [
        [1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,8,1,1,1,1,1,8,8,8,8,8,8],
        [1,8,1,1,1,1,1,1,1,1,1,1,8],
        [1,8,1,1,1,1,1,1,1,1,1,1,8],
        [1,8,1,1,1,1,1,1,1,1,1,1,8],
        [1,8,8,8,8,8,1,8,8,8,8,8,8],
        [1,1,1,1,1,8,1,8,1,1,1,1,1],
        [1,1,1,1,1,8,1,8,1,1,1,1,1],
        [1,1,1,1,1,8,1,8,1,1,1,1,1],
        [1,1,1,1,1,8,1,8,8,8,8,8,8]
    ]


    maze[a: a+10, b:b+13] = pattern

    x, y = (1, 1)
    maze[x, y] = 0
    stack = [(x, y)]
    while(stack):
        a, b = stack[-1]
        directions = [left, right, up, down]
        random.shuffle(directions)
        flage = 1
        for dir in directions:
            result  = dir(a, b, h, w, maze)
            if result :
                 flage = 0
                 stack.append(result)
                 break
        if flage:
            stack.pop()
             
    return maze

#print(creat_maze(10,10))


plt.figure(figsize=(50, 50))
plt.imshow(creat_maze(20, 20), cmap="binary")  # 'binary' turns 0 to white and 1 to black
plt.xticks([])  # Remove x-axis tick marks
plt.yticks([])  # Remove y-axis tick marks
plt.title("Maze Visualization")
plt.savefig('MaenIbrahim.PNG')
