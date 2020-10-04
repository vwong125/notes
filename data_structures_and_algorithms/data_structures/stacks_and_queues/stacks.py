"""
Implement a simple stack using a list
"""
class Stack:
    def __init__(self, stack = None):
        self.stack = stack if stack else []

    def pop(self):
        return self.stack.pop()
    
    def push(self, item):
        self.stack.append(item)

    def peek(self):
        return self.stack[len(self.stack) - 1]
    
    def isEmpty(self):
        return len(self.stack) == 0

def main():
    # test the stack class
    stack = Stack()
    stack.push(5)
    stack.push(10)
    print(stack.pop())
    print(stack.pop())


if __name__ == '__main__':
    main()