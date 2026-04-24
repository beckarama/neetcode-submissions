class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for bracket in s:
            if bracket in ["(", "{", "["]:
                stack.append(bracket)
            else:
                if not stack:
                    return False

                top = stack[-1]

                if bracket == ")" and top == "(":
                    stack.pop()
                elif bracket == "}" and top == "{":
                    stack.pop()
                elif bracket == "]" and top == "[":
                    stack.pop()
                else:
                    return False

        return len(stack) == 0