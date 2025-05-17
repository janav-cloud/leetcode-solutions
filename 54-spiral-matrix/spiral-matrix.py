class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        rows, cols = len(matrix), len(matrix[0])
        total = rows * cols
        
        top, bottom = 0, rows - 1
        left, right = 0, cols - 1
        
        while len(result) < total:
            for col in range(left, right + 1):
                if len(result) < total:
                    result.append(matrix[top][col])
            top += 1
            
            for row in range(top, bottom + 1):
                if len(result) < total:
                    result.append(matrix[row][right])
            right -= 1
            
            for col in range(right, left - 1, -1):
                if len(result) < total:
                    result.append(matrix[bottom][col])
            bottom -= 1
            
            for row in range(bottom, top - 1, -1):
                if len(result) < total:
                    result.append(matrix[row][left])
            left += 1
            
        return result