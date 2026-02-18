class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        res = []
        diags_counts = n + m - 1 + abs(m - n)
        diag_dir = 1
        for curr_diag  in range(diags_counts):
            diag = []
            i = min(curr_diag, m - 1)
            j = 0 if curr_diag < m else curr_diag - m  + 1
            print(i,j)
            while 0 <= i < m and 0 <= j < n:
                diag.append(mat[i][j])
                i -= 1
                j += 1
            res += diag[::diag_dir] 
            diag_dir *= -1


        return res


        