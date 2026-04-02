
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        islands = 0

        seen = set()

        def find_island(x, y):
            stack = []
            stack.append((x,y))
            # print(seen)
            while stack:
                
                x, y = stack.pop()
                seen.add((x,y))
                
                
                if x == 0:
                    pass
                elif grid[x-1][y] == "1" and (x-1, y) not in seen:
                    stack.append((x-1, y))
                
                if y == 0:
                    pass
                elif grid[x][y-1] == "1" and (x, y-1) not in seen:
                    stack.append((x, y-1))

                if x == len(grid)-1:
                    pass
                elif grid[x+1][y] == "1" and (x+1, y) not in seen:
                    stack.append((x+1, y))
                
                if y == len(grid[0])-1:
                    pass
                elif grid[x][y+1] == "1" and (x, y+1) not in seen:
                    stack.append((x, y+1))

            # print(seen)
                


            

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == "1" and (i, j) not in seen:
                    
                    find_island(i, j)
                    print(i,j, seen)
                    islands += 1

        return islands




        