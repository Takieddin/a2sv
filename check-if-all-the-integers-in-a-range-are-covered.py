class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        res = False
        for i in range(left, right + 1):
            res = False
            for start, end in ranges:
                if start <= i <= end:
                    res = True
            if not res:
                return False
        return True
        