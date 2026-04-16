class linkedlist:
    class node:
        def __init__(self, d):
            self.data = d
            self.next = None
    def __init__(self):
        self.head = None
    # to insert an element at beginning
    def insert_at_begin(self, d):
        newnode = self.node(d)
        if self.head is None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode
    # to insert at last
    def insert_at_end(self, d):
        newnode = self.node(d)
        if self.head is None:
            self.head = newnode
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newnode
    #to delete at end
    # to display a linked list
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ------------> ")
            temp = temp.next
        print("None")
if __name__ == "__main__":
    l = linkedlist()
    l.insert_at_begin(10)
    l.insert_at_begin(20)
    l.insert_at_begin(30)
    l.insert_at_end(40)
    l.insert_at_end(50)  
    l.display()