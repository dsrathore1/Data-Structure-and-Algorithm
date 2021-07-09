class BST:
    def __init__(self, key):
        self.lchild = None
        self.key = key
        self.rchild = None

    def insertion(self, data):
        if self.key is None:
            self.key = data
            return

        if self.key == data:
            return

        if data < self.key:
            if self.lchild:
                self.lchild.insertion(data)
            else:
                self.lchild = BST(data)

        else:
            if self.rchild:
                self.rchild.insertion(data)
            else:
                self.rchild = BST(data)

    def search(self, data):
        if data == self.key:
            print(f"{data} is found!")
            return
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print(f"{data} is not found!")

        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print(f"{data} is not found!")

    def preOrder(self):
        if self.key is not None:
            print(self.key, end=" ")
        if self.lchild is not None:
            self.lchild.preOrder()
        if self.rchild is not None:
            self.rchild.preOrder()

    def inOrder(self):
        if self.lchild is not None:
            self.lchild.inOrder()
        if self.key is not None:
            print(self.key, end=" ")
        if self.rchild is not None:
            self.rchild.inOrder()

    def postOrder(self):
        if self.lchild is not None:
            self.lchild.postOrder()
        if self.rchild is not None:
            self.rchild.postOrder()
        if self.key is not None:
            print(self.key, end=" ")

    def get_min(self):
        current = self
        while current.lchild is not None:
            current = current.lchild
        return (current.key)

    def get_max(self):
        while self.rchild is not None:
            self = self.rchild
        return (self.key)

    def deletion(self, data):
        if self.key is None:
            print("Tree is Empty")
            return
        if data < self.key:
            if self.lchild is not None:
                self.lchild = self.lchild.deletion(data)
            else:
                print("Your given data is not present into the Left Sub-tree!")
        elif data > self.key:
            if self.rchild is not None:
                self.rchild = self.rchild.deletion(data)
            else:
                print ("Your given data is not present into the Right Sub-Tree!")

        else:
            if self.lchild is None and self.rchild is None:
                return None
            if self.lchild is None:
                return self.rchild
            if self.rchild is None:
                return self.rchild
            
            min_val = self.rchild.get_min()
            self.key = min_val
            self.rchild = self.rchild.deletion(min_val)
        
        return self


root = BST(100)

list1 = [50, 75, 74, 76, 73, 150, 125, 124, 130, 131]

for i in list1:
    root.insertion(i)

print("Pre-Order")
root.preOrder()

print('\n')
print("In-Order")
root.inOrder()

print('\n')
print("Post-Order")
root.postOrder()

print('\n')
print("The min value of the tree is : ", root.get_min())


print("\nThe max value of the tree is : ", root.get_max())


print("\n")
root.deletion(150)
root.inOrder()


print("\n")
root.search(50)