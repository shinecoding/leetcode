class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search on the row
        # binary search on the column
        # logm + logn
        t, b = 0, len(matrix) - 1
        while t<= b:
            row = t + (b-t)//2
            if matrix[row][-1] < target:
                t = row + 1
            elif matrix[row][0] > target:
                b = row - 1
            else:
                break
            
        if not (t <= b):
            return False
        
        row = (t+b)//2
        l, r = 0, len(matrix[0]) -1
        while l<=r:
            m = l + (r-l)//2
            if matrix[row][m] < target:
                l = m + 1
            elif matrix[row][m] > target:
                r = m - 1
            else:
                return True
            
        return False
