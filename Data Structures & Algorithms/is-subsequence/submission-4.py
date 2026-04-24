class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True

        stack = list(s)

        for i in range(len(t)-1, -1, -1):
            if stack != [] and t[i] == stack[-1]:
                stack.pop()
        return len(stack) == 0
            
        