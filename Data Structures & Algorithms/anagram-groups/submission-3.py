class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        anagrams = defaultdict(list)

        for word in strs:
            char_count = [0] * 26
            for c in word:
                idx = ord(c) - ord('a')
                char_count[idx] += 1
            anagrams[tuple(char_count)].append(word)
        
        for an in anagrams.values():
            res.append(an)
        return res