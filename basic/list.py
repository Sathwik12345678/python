#lists
l = [1,2,2,2.1,"prasad"]
print(type(l))
print(l)
#list indexing
l=[10,20,30,40]
print(l[0])
print(l[-4])
#list slicing
l=[10,20,30,40]
print(l[1:3])
print(l[:3])
print(l[2:3])
print(l[1:])
#cancadination operator
l1 = [1,2,3]
l2 = [4,5,6]
print(l1+l2)
#repetition
l=[1,2,3]
print(l*3)
#repetition
l=[10,20,30,40]
print([10,20,30,40]*3)
#member ship operator
l=[10,20,30,40]
print(30 in l)
print(10 in l and 40 in l)
#list methods
#1.append
l=[1,2,3,4,5,6]
l.append(6)
print(l)
#2.insert
l=[1,2,3,4,5]
l.insert(2,10)
print(l)
#.pop element
l=[1,2,3,4,5]
print(l.pop(2))
print(l)
#4.extend
l1=[1,2,3]
l1.extend([4,5,6])
print(l1)
#remove
l=[1,2,3,4,5,6]
l.remove(3)
print(l)
#map
from functools import reduce


l=[1,2,3,4,5,6]
print(list(map(lambda x:x**2,l)))
#filter
l=[1,2,3,4,5,6,7]
print(list(filter(lambda x : x%2 == 0,l)))
#reduce
l=[1,2,3,4,5,6]
result = reduce(lambda x,y: x+y,l)
print(result)