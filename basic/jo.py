"""write a program to find sum of digits of strings characters using filter map and reduce functions"""
from functools import reduce
li = ['a1bc2','3d9e7f','world','hello','123gh1i','9jk8l','7mno3']
def sum(s):
  digit = list(map(int,filter(lambda x:x.isnumeric(),s)))
  return reduce(lambda x,y:x+y,digit,0)
result = list(map(sum,li))
print(result)