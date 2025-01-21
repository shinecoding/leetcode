class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                # save the topLeft
                topLeft = matrix[l][l+i]

                # bottom left to top left
                matrix[l][l+i] = matrix[r-i][l]
                
                #bottom right to bottom left
                matrix[r-i][l] = matrix[r][r-i]
                
                #top right to bottom right
                matrix[r][r-i] = matrix[l+i][r]
                
                # top left to top right
                matrix[l+i][r] = topLeft
            # move to the smaller squre
            l += 1
            r -= 1
             
        return matrix