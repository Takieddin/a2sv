class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        

                  

        # output 
        n = len(gas)  # 5
        current = 0 # 0
        start = 0 # 0
        tank = 0 # 0
        visited = 0 # 0

        steps = 0 # 0
        while  visited < 2 * n : #  1 <11
            if tank < 0:
                steps = 0
                start = current # 1
                tank = 0
            tank += gas[current] - cost[current] # -3
            if current == start and steps > 0: # 0 == 5:
                return start 

            current = (current + 1) %  n
            visited += 1 # 1
            steps += 1 # 1
        return -1


        