name = "Kiran"
age = 20

print(f"My name is {name} and my age is {age}")
print("My name is {} and my age is {}".format(name,age))
print("My name is %s and my age is %d"%(name,age))
#generate a list of odd value which are less than given the number and display them
#solution 1
num = int(input())
ans = []
for value in range(1,num,2):
    ans.append(value)
print(ans)
#solution 2
n = int(input())
odd = []
for i in range(n):
  if i%2!=0:
    i == odd 
print(odd)

#bitwise operator
import time
n = int(input())
start = time.time()
odd = []
for i in range(n):
  if i&1:
    odd.append(i)
print(odd)
end = time.time()
tot_time = end - start
#using list comprehension used for generating a sequence in a faster manner compared to traditional approach
n = int(input())
start = time.time()
odd = [i for i in range(n) if i%2!=0]
print(odd)
end = time.time()
tot_time = end - start
"""
&-used for checking states
|-used for setting states
^-used for toggling states
<<-left shift
>>-right shift
"""
"""exception handling means handling the errors is know as exceptional handling
exceptions are group of errors which stops the execution 
the exceptions are two types 1. run time exceptions 2. compile time exceptions
run time exceptions are uncontrollable features ex: thread,dead
compiler exceptions can be avoided and can be controlled using exceptional handling
the statements are classified into two types 1.normal statements 2.critical statements
normal statements: which will not generate any error ex: n =100
critical statements: which may generate an error ex: n = int('1000c')
exceptional handling is done with 4 different blocks 1st. try used for writing critical statements 
2. except will be executed when the try block reserves an error
3. else will be executed when there is no error in try block
4.finally will be executed always irrespective of which block is executed generally used for closing resources
example: wap to find out position of occurance of a value for the second time inside a list (each item repeats one time)
"""
list = [1,2,3,4,3,2,1]
n = int(input())
try:
  second = list.index(n,list.index(n)+1)
except Exception:
  print("second occurance not found")
else:
  print(second)
print(second)
