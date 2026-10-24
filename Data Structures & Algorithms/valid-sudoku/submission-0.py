class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        blocks : dict[tuple, List[str]] = {}

        for i in range(9):
            line = set()
            column = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in line:
                        return False
                    else:
                        line.add(board[i][j])
                        if (i//3, j//3) not in blocks:
                            blocks[(i//3, j//3)] = [board[i][j]]
                        else:
                            if board[i][j] in blocks[(i//3, j//3)]:
                                return False
                            else:
                                blocks[(i//3, j//3)].append(board[i][j])
                if board[j][i] != ".":
                    if board[j][i] in column:
                        return False
                    else:
                        column.add(board[j][i])
        return True