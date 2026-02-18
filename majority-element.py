class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        res = -1
        freq = 0
        for num in nums:
            if counts[num] > freq:
                freq = counts[num]
                res = num
        return res
        