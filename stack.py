class Stack:
    def __init__(self):
        self.stack = []

    def push(self, d):
        self.stack.append(d)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        raise IndexError("pop from empty stack")
    def is_empty(self):
        return len(self.stack) == 0
if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    print(s.pop())  
    print(s.pop())  
    print(s.is_empty())  
    print(s.pop()) 
    print(s.is_empty())
