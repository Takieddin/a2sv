class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = Counter(words[0])
        for word in words[1:]:
            word_c = Counter(word)

            for let in common.keys():
                common[let] = min(common[let], word_c[let])
        res = []
        for k,v in common.items():
            for i in range(v):
                res.append(k)
        return res
        