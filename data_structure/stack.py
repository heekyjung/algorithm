class Stack:
    items =  []
    top = -1
    
    def __init__(self, size): # createStack
        self.size = size
        self.items = [False for s in range(size)]
    
    def is_empty(self):
        return self.top == -1
    
    def is_full(self):
        return self.top == self.size - 1
    
    def push(self, item):
        if self.is_full():
            print("Stack is full.")
        else:
            self.top += 1
            self.items[self.top] = item
    
    def pop(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            self.items[self.top] = False
            self.top -= 1
    
    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            return self.items[self.top]


    def display(self):
        print(self.items)


my_stack = Stack(3)
my_stack.display()

my_stack.pop() # stack is empty 출력

my_stack.push(8)
my_stack.push(2)
my_stack.display()
my_stack.push(7)
my_stack.display()
my_stack.push(6) # stack is full 출력

print(my_stack.peek())
