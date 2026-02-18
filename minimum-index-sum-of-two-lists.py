class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        n, m = len(list1), len(list2)
        idx_sum = n + m
        res = []
        for i in range(n):
            for j in range(m):
                if list1[i] == list2[j] and i + j <= idx_sum:
                    if i + j < idx_sum:
                        res = []
                        idx_sum = i + j
                    res.append(list1[i])
        return res 


        
        