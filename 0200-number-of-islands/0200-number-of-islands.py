from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        island = 0

        def bfs(r, c):
            q = deque()
            visit.add((r,c))
            q.append((r,c))

            while q:
                x, y = q.popleft()
                directions = [(0,1),(1,0),(0,-1),(-1,0)]
                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy

                    if nx in range(rows) and ny in range(cols) and grid[nx][ny] == "1" and (nx, ny) not in visit:
                        q.append((nx, ny))
                        visit.add((nx, ny))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r, c)
                    island += 1
        
        return island