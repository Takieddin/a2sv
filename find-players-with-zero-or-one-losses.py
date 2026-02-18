class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        played = set()
        lost = {}
        not_lost = []
        lost_one = []
        max_player = -1
        for match in matches:
            played.add(match[0])
            played.add(match[1])
            lost[match[1]] = lost.get(match[1], 0) + 1
            max_player = max(max_player, match[0], match[1])
        for i in range(1, max_player + 1):
            if i in played:
                if i not in lost:
                    not_lost.append(i)
                elif lost[i] == 1:
                    lost_one.append(i)
        return [not_lost, lost_one]



        