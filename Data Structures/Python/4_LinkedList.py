class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        last = self.head
        while last.ref:
            last = last.ref
        last.ref = new_node


    def add_between(self, prev_node, data):
        if prev_node is None:
            print("The previous node is must be LinkedList!")
            return
        
        new_node = Node(data)
        new_node.ref = prev_node.ref
        prev_node.ref = new_node

    def printing(self):
        n = self.head
        while n is not None:
            print(n.data, "-->", end=" ")
            n = n.ref
        print("None")


ll = LinkedList()

ll.add_begin(10)
ll.add_begin(20)
ll.add_begin(30)
ll.add_begin(40)
ll.add_begin(50)
ll.add_begin(60)
ll.add_begin("Begin")


ll.add_end(9)
ll.add_end(8)
ll.add_end(7)


ll.add_between(ll.head.ref, 1000)

ll.printing()
