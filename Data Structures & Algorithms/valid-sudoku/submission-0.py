from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        q1 = defaultdict(int)
        q2 = defaultdict(int)
        q3 = defaultdict(int)


        for i, row in enumerate(board):
            valid_row = defaultdict(int)
            valid_col = defaultdict(int)
            print(i, row)
            if (i) // 3 == 1:
                
                q1 = defaultdict(int)
                q2 = defaultdict(int)
                q3 = defaultdict(int)



            for j, num in enumerate(row):
                if num != "." and valid_row[num] > 0:
                    print("l1", valid_row)
                    return False
                valid_row[num] += 1

                if board[j][i] != "." and valid_col[board[j][i]] > 0:
                    print("l2")
                    return False
                valid_col[board[j][i]] += 1

                if j < 3:
                    if num != "." and q1[num] > 0:
                        return False
                    q1[num] += 1
                
                elif num != "." and j < 6:
                    if q2[num] > 0:
                        return False
                    q2[num] += 1

                elif num != ".":
                    if q3[num] > 0:
                        return False
                    q3[num] += 1




        return True
                

        