"""queue implementation"""
#q = []
# q.insert(0,10)
# q.insert(0,20)
# q.insert(0,30)
# print(q)
# print(q.pop())
# print(q)
# print(q.pop())
# print(q)
"""using class and obj"""
class queue:
  def __init__(self):
    self.items = []
  def enqueue(self,item):
    self.items.insert(0,item)
  def dequeue(self):
    self.items.pop()
  def peek(self):
    print(self.items[-1])
  def display(self):
    print(self.items)
q = queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
q.dequeue()
q.display()
q.peek()