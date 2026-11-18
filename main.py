from MazeGen import MazeGeneartor
ob = MazeGeneartor(10,10,False)
maze = ob.generate_maze()
print(maze)
ob.shortest_path((1,2), (3,3))