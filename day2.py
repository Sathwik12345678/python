def add(ele,li = None):
    if li is None:
        li = []
    li.append(ele)
    print(li)
add(6)
add(7,[])
"""slash as function"""
"""write a program to find number of digits for a integer number"""
n = int(input("Enter a number: "))
count = 0
while n!=0:
  n = n // 10
  count += 1 
print(count)
"""Way 2 """
n = int(input("Enter a number: "))
count = 0
divisor = 1
while (n//divisor)>0:
  divisor *= 10
  count += 1
print(count)
"""Way - 3 """
from math import log10
n = int(input("Enter a number: "))
count = int(log10(n)+1)
print(count)
"""converting to function """
def count_digits(n):
  count = int(log10(n)+1)
  return count
count_digits(123456)