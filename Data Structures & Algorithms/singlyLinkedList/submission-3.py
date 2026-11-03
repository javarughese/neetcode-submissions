class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None  
    
    def get(self, index: int) -> int:
        i = 0
        node = self.head

        if (self.head == None or index < 0 ):
            return -1

        while (i < index and node.next != None):
            node = node.next
            i+=1

        if(index > i):
            return -1

        return node.value
        

    def insertHead(self, val: int) -> None:
        newHead = Node(val)
        newHead.next = self.head
        self.head = newHead

    def insertTail(self, val: int) -> None:
        if (self.head == None):
            new = Node(val)
            self.head = new
            return

        node = self.head
        while (node.next != None):
            node = node.next
        newNode = Node(val)
        node.next = newNode

    def remove(self, index: int) -> bool:
        node = self.head

        if (index < 0 or node == None):
            return False
        
        if(index == 0): 
            self.head = node.next
            return True

        for i in range(index-1):
            if (node.next == None):
                return False
            else: 
                node = node.next
        
        if (node.next == None):
            return False

        node.next = node.next.next 
        return True

    def getValues(self) -> List[int]:
        arr = []
        node = self.head

        if(self.head == None):
            return []

        while (node != None):
            arr.append(node.value)
            node = node.next
        return arr
        