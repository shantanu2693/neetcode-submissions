class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        count_row = defaultdict(int)
        for i,row in enumerate(board):
            count_row.clear()
            for j in range(len(row)):
                if (board[i][j] == "."):
                    continue
                count_row[int(board[i][j]) - 1] += 1
            if any(count > 1 for count in count_row.values()): 
                return False
        
        count_col = defaultdict(int)
        for i,row in enumerate(board):
            count_col.clear()
            for j in range(len(row)):
                if (board[j][i] == "."):
                    continue
                count_col[int(board[j][i]) - 1] += 1
            if any(count > 1 for count in count_col.values()): 
                return False 

        count_box = defaultdict(int)
        for m in [0,3,6]:
            for n in [0,3,6]:
                count_box.clear()
                for i in range (m,m+3):
                    for j in range(n,n+3):
                        if (board[i][j] == "."):
                            continue
                        count_box[int(board[i][j])] += 1
                        if any(count > 1 for count in count_box.values()): 
                            return False

        return True
