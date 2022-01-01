class Node:
    def __init__(self, data):
        self.data = data,
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None
    def print_LL(self):
        if self.head is None:
            print("linked List is Empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref
            
LL = LinkedList()
node1 = Node(12)
LL.print_LL()
