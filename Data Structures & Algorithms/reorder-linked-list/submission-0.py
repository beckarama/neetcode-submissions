# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = [] 
        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next
        
        cur = head
        for i in range(len(stack) // 2):
            next_node = cur.next
            stack[i].next = stack[-1]
            stack[-1].next = next_node
            stack.pop()
            cur = next_node
        cur.next = None
        