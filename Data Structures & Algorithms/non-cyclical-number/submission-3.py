class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(num):
            total = 0

            for digit in str(num):
                total += int(digit) ** 2
            return total
        
        slow = fast = n

        while fast != 1:
            slow = get_next(slow)
            fast = get_next(get_next(fast))

            if slow == fast and fast != 1:
                return False
        return True
