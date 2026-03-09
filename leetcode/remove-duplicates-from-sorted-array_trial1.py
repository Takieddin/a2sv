class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1, p2 = 0, 1
        if len(nums) <= 1:
            return 1
        while p2 < len(nums):
            if nums[p2] == nums[p1]:
                p2 += 1
                continue
            nums[p1 + 1] = nums[p2]
            p1 += 1
            p2 += 2
        return p1 + 1
        
        