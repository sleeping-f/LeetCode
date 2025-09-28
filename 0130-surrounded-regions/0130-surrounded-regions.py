class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        ROW = len(board)
        COL = len(board[0])
        q = deque()
        
        for i in range(ROW):
            if board[i][0] == 'O': q.append((i, 0))
            if board[i][COL-1] == 'O': q.append((i, COL-1))
        for i in range(COL):
            if board[0][i] == 'O' and i != 0 and i != COL-1: q.append((0, i))
            if board[ROW-1][i] == 'O' and i != 0 and i != COL-1: q.append((ROW-1, i))


        while q:
            print(q)
            row, col = q.popleft()
            board[row][col] = "C"

            if row > 0 and board[row-1][col] == 'O': q.append((row-1, col))
            if col > 0 and board[row][col-1] == 'O': q.append((row, col-1))
            if row < ROW-1 and board[row+1][col] == 'O': q.append((row+1, col))
            if col < COL-1 and board[row][col+1] == 'O': q.append((row, col+1))

            

        print(board)
        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'C':
                    board[i][j] = 'O'

        print(board)