class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        m = len(nums)
        n = len(nums[0])
        res = 0
        for i in range(m):
            nums[i].sort()
        for j in range(n -1, -1, -1):
            max_num = -1
            for i in range(m):
                max_num = max(max_num, nums[i][j])
            res += max_num
        return res
        