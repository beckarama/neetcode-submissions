class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        positions = defaultdict(list)

        for s in strs:
            pos = [0] * 26
            for c in s:
                idx = ord(c) - ord("a")
                pos[idx] += 1
            positions[tuple(pos)].append(s)
        return (list(positions.values()))
        
