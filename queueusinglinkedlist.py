"""queue using linked list"""
class queue:
  class node:
    def __init__(self,d):
      self.data = d
      self.next = None
  def __init__(self):
      self.head = None
      self.end = None
  def enqueue(self,item):
    newnode = self.node(item)
    if self.head is None:
      self.head = newnode
      self.end = newnode
    else:
      self.end.next = newnode
      self.end = newnode
  def dequeue(self):
    if self.head is None:
      print("queue is empty")
    else:
      temp =  self.head
      self.head = self.head.next
      if self.head is None:
        self.end = None
      print(f"{temp.data} is removed")
  def peek(self):
    if self.head is None:
      print("queue is empty")
    else:
      print(self.head.data)
  def is_empty(self):
    return self.head is None
  def display(self):
    temp = self.head
    while temp is not None:
      print(temp.data,end="------->")
      temp = temp.next
    print("None")
q = queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.display()
q.dequeue()
q.display()
q.peek()
print(q.is_empty())
#enque time comp:O(1)
#dequeue time comp:O(1)
#total time comp of queue using linkedlist:O(1)
