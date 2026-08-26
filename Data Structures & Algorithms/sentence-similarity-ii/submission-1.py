class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        
        adj = defaultdict(list)
        for w1, w2 in similarPairs:
            adj[w1].append(w2)
            adj[w2].append(w1)
        
        visit = set()
        def dfs(word, target, visit):
            if word == target:
                return True
            if word in visit:
                return False
            
            visit.add(word)
            for nei in adj[word]:
                if dfs(nei, target, visit):
                    return True
            return False

        for i, w in enumerate(sentence1):
            visit = set()
            if not dfs(w, sentence2[i], visit):
                return False
        return True


        