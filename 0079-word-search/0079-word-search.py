class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visit = set()

        def dfs(r,c,i):
            # 완료 조건
            if i == len(word):
                return True
            if (c < 0 or r < 0 or 
                c >= COLS or r >= ROWS or 
                board[r][c] != word[i] or 
                (r,c) in visit):
                return False

            visit.add((r,c))
            res = (dfs(r-1,c,i+1) or
                    dfs(r+1,c,i+1) or
                    dfs(r,c-1,i+1) or
                    dfs(r,c+1,i+1))
            visit.remove((r,c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True
        return False