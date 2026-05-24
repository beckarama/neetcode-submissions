class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        largest_area = 0
        heights = heights + [0]

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] >= h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1

                largest_area = max(largest_area, height * width)
            stack.append(i)
        return largest_area