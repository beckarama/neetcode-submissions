class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        cur = self.head
        i = 0

        while cur:
            if i == index:
                return cur.val
            cur = cur.next
            i += 1

        return -1


    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        

    def remove(self, index: int) -> bool:
        if not self.head:
            return False

        if index == 0:
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return True

        cur = self.head
        i = 0

        while cur and cur.next:
            if i + 1 == index:
                if cur.next == self.tail:
                    self.tail = cur
                cur.next = cur.next.next
                return True
            cur = cur.next
            i += 1

        return False
        
    def getValues(self) -> List[int]:
        cur = self.head
        vals = []
        while cur:
            vals.append(cur.val)
            cur = cur.next
        return vals
        


