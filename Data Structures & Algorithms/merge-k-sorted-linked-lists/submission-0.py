# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        
        for i, l in enumerate(lists):
            if l is not None:
                heapq.heappush(minHeap, (l.val, i))
        
        dummy = cur = ListNode()
        while minHeap:
            val, index = heapq.heappop(minHeap)
            cur.next = ListNode(val)
            cur = cur.next

            if lists[index].next:
                lists[index] = lists[index].next
                heapq.heappush(minHeap, (lists[index].val, index))
        return dummy.next
        
            
        