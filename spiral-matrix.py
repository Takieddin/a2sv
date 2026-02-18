class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        up, down, left, right = -1 , n, -1, m
        res = []
        
        while len(res) < n * m:
            if up + 1 < down:
                for i in range(left + 1, right):
                    res.append(matrix[up + 1][i])
                up += 1
            
            if right - 1 > left:
                for i in range(up + 1, down):
                    res.append(matrix[i][right - 1])
                right -= 1
            
            if down - 1 > up:
                for i in range(right - 1, left, -1):
                    res.append(matrix[down - 1][i])
                down -= 1
            
            if left + 1 < right:
                for i in range(down - 1, up, -1):
                    res.append(matrix[i][left + 1])
                left += 1
                
        return res