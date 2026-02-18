class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_map = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        transformations = set()
        for w in words:
            shift = ord("a")
            t = ""
            for let in w:
                t += morse_map[ord(let) - shift]
            transformations.add(t)
        return len(transformations)