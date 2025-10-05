class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            row_seen = set()
            col_seen = set()
            for j in range(9):
                r = board[i][j]
                if r != '.':
                    if r in row_seen:
                        return False
                    row_seen.add(r)

                c = board[j][i]
                if c != '.':
                    if c in col_seen:
                        return False
                    col_seen.add(c)

        for br in range(0, 9, 3):
            for bc in range(0, 9, 3):
                row_seen = set()
                for r in range(br, br + 3):
                    for c in range(bc, bc + 3):
                        val = board[r][c]
                        if val != '.':
                            if val in row_seen:
                                return False
                            row_seen.add(val)

        return True