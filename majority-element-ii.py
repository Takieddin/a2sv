class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = Counter(nums)
        res = set()

        for num in nums:
            if counts[num] > n / 3:
                res.add(num)
        return list(res)