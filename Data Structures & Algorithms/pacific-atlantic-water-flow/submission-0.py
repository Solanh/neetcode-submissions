

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        connect = []

        def check(x,y):
            seen = set()

            s = []
            s.append((x,y))

            p = False
            a = False

            

            while s:
                x, y = s.pop()
                seen.add((x,y))
                val = heights[x][y]
                

                if x == 0:
                    p = True
                if y == 0:
                    p = True
                if x == len(heights) -1:
                    a = True
                if y == len(heights[0]) -1:
                    a = True

                if a and p:
                    return True

                
                if x > 0 and heights[x-1][y] <= val and (x-1,y) not in seen:
                    s.append((x-1, y))

                if x < len(heights)-1 and heights[x+1][y] <= val and (x+1,y) not in seen:
                    s.append((x+1, y))
                
                if y > 0 and heights[x][y-1] <= val and (x,y-1) not in seen:
                    s.append((x, y-1))

                if y < len(heights[0]) -1 and heights[x][y+1] <= val and (x,y+1) not in seen:
                    s.append((x, y+1))
                
                    

                




            return True if a and p else False





        for i in range(len(heights)):
            for j in range(len(heights[i])):
                valid = check(i, j)
                if valid:
                    connect.append([i, j])

        return connect

                



        