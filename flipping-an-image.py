class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # def inv(i):
          #  return 0 if i else 1
        return [[int( not x) for x in row[::-1] ] for row in image]