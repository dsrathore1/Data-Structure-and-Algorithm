# Queue using list
print ('Queue using list')

queue = []

queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)
queue.append(50)

print(queue)

queue.pop(0)

print(queue)




# Queue using Class

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue (self, data):
        return self.queue.insert(0, data)
    
    def dequeue(self):
        return self.queue.pop()

    def length(self):
        print(len(self.queue))

    def peek(self):
        print(self.queue[0])

    def printing (self):
        print(self.queue)

if __name__ == '__main__':
    q = Queue()

    q.enqueue(19)
    q.enqueue(13)
    q.enqueue(14)
    q.enqueue(195)
    q.enqueue(15)

    print('\nQueue is : ')

    q.printing()

    print('\nPop first element :')

    q.dequeue()

    q.printing()

    print('\nLength of the element is :')

    q.length()

    print('\nPeek element is :')

    q.peek()


# Queue using Function
queue = []


def enqueue():
    element = int(input())
    queue.append(element)
    print(element, "Element is added")


def dequeue():
    if queue == [] or not queue:
        print("Queue is empty")
    else:
        return queue.pop(0)


def length():
    print(len(queue))


def display():
    print(queue)




if __name__ == '__main__':
    while True:
        print("Choice any one of them \n1.Enqueue\n2. Dequeue\n3. Display\n4. Length\n5. exit")
        print('\n')
        choice = int(input())
        if choice == 1:
            print('\nAdding an element')
            enqueue()
            print('\n')
        elif choice == 2:
            print('\nRemoving an element')
            dequeue()
            print('\n')
        elif choice == 3:
            print('\nYour Queue is :')
            display()
            print('\n')
        elif choice == 4:
            print('\nYour Queue lenght is : ')
            length()
            print('\n')
        elif choice == 5:
            print("\nOOPs you're out ")
            break
        else:
            print("You Enter Wrong Entity")
