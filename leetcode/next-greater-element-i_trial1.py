class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        greater_next = {}
        for num in nums2:
            while stack and stack[-1] <= num:
                greater_next[stack.pop()] = num
            stack.append(num)
        res = []
        for num in nums1:
            res.append(greater_next.get(num, -1))
        return res