from maze import *
from exception import *
from stack import *
class PacMan:
    def __init__(self, grid : Maze) -> None:
        ## DO NOT MODIFY THIS FUNCTION
        self.navigator_maze = grid.grid_representation
        
    def find_path(self, start , end):
        mystack = Stack()
        mystack.push(start)
        
        m = len(self.navigator_maze)
        n = len(self.navigator_maze[0])
        
        #initialising visited matrix False and maintaing it for each point we have visited
        visited = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(False)
            visited.append(row)
            
        visited[start[0]][start[1]] = True
        
        #boundary cases
        if(self.navigator_maze[start[0]][start[1]] == 1):
            raise PathNotFoundException
        if(self.navigator_maze[end[0]][end[1]] == 1):
            raise PathNotFoundException
        if(start == end):
            return list(mystack)
            
            
        while mystack.size() > 0:
            x, y = mystack.top()

        #if destination is reached
            if (x, y) == end:
                return list(mystack) 
                
            moved = False

        # Check leftward
            if x > 0 and not visited[x-1][y] and self.navigator_maze[x-1][y] == 0:
                mystack.push((x-1, y))
                visited[x-1][y] = True
                moved = True

        # Check upward
            elif y > 0 and not visited[x][y-1] and self.navigator_maze[x][y-1] == 0:
                mystack.push((x, y-1))
                visited[x][y-1] = True
                moved = True

        # Check rightward
            elif x < m-1 and not visited[x+1][y] and self.navigator_maze[x+1][y] == 0:
                mystack.push((x+1, y))
                visited[x+1][y] = True
                moved = True

        # Check downward
            elif y < n-1 and not visited[x][y+1] and self.navigator_maze[x][y+1] == 0:
                mystack.push((x, y+1))
                visited[x][y+1] = True
                moved = True

            if not moved:
                mystack.pop()  # Backtrack if no move is possible
        raise PathNotFoundException 
        
                
       
        
 
        
        
        
        
        
