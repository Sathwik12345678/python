#stack implimentation using linked list
class stack:
    class node:
        def __init__(self, d):
            self.data = d
            self.next = None
    def __init__(self):
        self.top = None
    def push(self, d):
        newnode = self.node(d)
        newnode.next = self.top
        self.top = newnode
    def pop(self):
        if self.top is None:
            raise IndexError("pop will not work on empty stack")
        temp = self.top
        self.top = self.top.next 
        return temp.data
    def peek(self):
        if self.top is None:
            raise IndexError("peek will not apply on empty stack")
        return self.top.data
    def is_empty(self):
        return self.top is None
    def display(self):
        temp = self.top
        while temp is not None:
            print(temp.data)
            temp = temp.next
if __name__ == "__main__":
    s = stack() 
    print("Is stack empty?", s.is_empty()) 
    s.push(10)
    s.push(20)
    s.push(30)
    print("Stack elements:")
    s.display()
    print("After pop:")
    s.pop()
    print("Top element:", s.peek())
    s.display() 
#merge two sorted linked
# list and find loop in linkedlist