class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr_sorted = sorted(nums)
        res = {}
        for i in range(len(nums)):
            if arr_sorted[i] not in res:
                res[arr_sorted[i]] = i
        ans = []
        for i in range(len(nums)):
            ans.append(res[nums[i]])
        return ans

        