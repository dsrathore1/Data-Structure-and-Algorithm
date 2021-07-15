# Stack using List
print('Stack using List\n')
stack = []

stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
stack.append(50)

print(stack)

stack.pop()

print(stack)

print('\n')


# Stack using Function

print('Stack using Function\n')

list3 = []

def push(data):
    return list3.append(data)
def printing():
    print(list3)

push(10)
push(20)
push(30)
push(40)
push(50)

printing()


print('\n')

print('Stack Using Class\n')

class Stack:

    list1 = []

    def push(self, data):
        return self.list1.append(data)

    def remove(self):
        return self.list1.pop()

    def isEmpty(self):
        return True if self.list1 is None else False

    def finding(self, key):
        if (key in self.list1):
            print(f'{key} is available into a Stack')

        else:
            print(f'{key} is not available into a Stack')

    def printing(self):
        print(self.list1)


stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)


stack.printing()
print('\n')
stack.finding(10)
print('\n')
print('Stack is Empty? ', stack.isEmpty())