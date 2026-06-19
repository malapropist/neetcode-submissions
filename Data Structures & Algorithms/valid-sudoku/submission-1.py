class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check rows & columns
        col_c = {i:[] for i in range(9)}
        for row in board:
            checkset = set()
            for cell,val in enumerate(row):
                if val in checkset and val!='.':
                    return False
                checkset.add(val)
                if val in col_c[cell] and val!='.':
                    return False
                col_c[cell].append(val)
        #check boxes
        for x in range(3):
            for y in range(3):
                cbox = []
                print(x,y)
                for z in range(3*x,3*x+3):
                    for a in range(y*3,3*y+3):
                        val = board[z][a]
                        if val in cbox and val !='.':
                            return False
                        cbox.append(val)
                # print(cbox)
        return True