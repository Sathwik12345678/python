"""write a function which finds sum of digits for a single number"""
def sum_of_digits(n):
    sum = 0
    while n>0:
        digit = n % 10
        sum += digit
        n = n // 10
    return sum
result = int(input("enter a number:"))
print(sum_of_digits(result))
"""reduced code"""
def add(num):
    sol = 0
    while num>0:
        sol += num%10
        num //= 10
    return sol
num = int(input("Enter a number: "))
print(add(num))
"""for list using map function"""
def add(num):
    sol = 0
    while num>0:
        sol += num%10
        num //= 10
    return sol
li = list(map(int,input("enter the numbers:").split()))
ans = list(map(add,li))
print(ans)
"""given a list of strings with numreic values and non numeric values , filter all the numeric strings and convert them to integers use filter and map functions"""
"""using for loop"""
li = ['123', 'abc', '456', 'def', '789', 'hello', '147']
ans = []
for i in li:
    if i.isnumeric():
        ans.append(int(i))
print(ans)
"""using filter and map functions"""
li = ['123', 'abc', '456', 'def', '789', 'hello', '147']
ans = list(map(int,filter(lambda x:x.isnumeric(),li)))
"""function for adding up all the ord values of  the supplied characters inside a string"""
"""sol 1"""
st = 'abcd'
sol = 0
for char in st:
    sol += ord(char)
print(sol)
"""sol2"""
from functools import reduce
from string import digits
def add(num,char):
    return num + ord(char)
st = 'abcd'
sol = reduce(add,st,0)
print(sol)
"""write a program to find sum of digits of strings characters using filter map and reduce functions"""
from functools import reduce
li = ['a1bc2','3d9e7f','world','hello','123gh1i','9jk8l','7mno3']
def sum(s):
    digit = list(map(int,filter(lambda x:x.isnumeric(),s)))
    return reduce(lambda x,y:x+y,digit,0)
result = list(map(sum,li))
print(result)
"""or"""
from functools import reduce
def seperate(ele):
    ans = ''
    for char in ele:
        if char.isdigit():
            ans += char
    return ans
def is_valid(ele):
    if ele !='':
        return True
    else:
        return False
li = ['a1bc2','3d9e7f','world','hello','123gh1i','9jk8l','7mno3']
ans = list(map(seperate,li))
ans2 = list(filter(is_valid,ans))
ans3 = list(map(int,ans2))
print(ans3)
ans4 = reduce(lambda n1,n2: n1+n2,ans3,0)
print(ans4)
"""Given a list of strings, extract digits from each string, keep only even digits, and find their total sum. """
from functools import reduce
def even_sum(ele):
    ans = ''
    for char in ele:
        if char.isdigit() and int(char)%2==0:
            ans+=char
    return ans
def is_valid(ele):
    if ele !='':
        return True
    else:
        return False
li = ['ab12', '9x8', 'hello5', '246', '7z']
ans = list(map(even_sum,li))
ans2 = list(filter(is_valid,ans))
ans3 = list(map(int,ans2))
print(ans3)
ans4 = reduce(lambda x1,x2:x1+x2,ans3,0)
"""Using map, filter, and reduce, count how many digits are present in the list."""
from functools import reduce
def count_digit(ele):
    count = 0
    for char in ele:
        if char.isdigit():
            count += 1
    return count
li = ['a1b2c3', 'xyz', '98k', 'hello']
ans = list(map(count_digit,li))
sum_of_digitcount = reduce(lambda x,y:x+y,ans,0)
print(ans)
"""Extract digits from strings and find the product of all digits."""
from functools import reduce
def extract_digits(ele):
    digits = []
    for char in ele:
        if char.isdigit():
            digits.append(int(char))
    return digits
li = ['a1b2', '3c4d', 'e5f6']
all_digits = []
for item in li:
    all_digits.extend(extract_digits(item))
product_of_digits = reduce(lambda x,y:x*y,all_digits,1)
print(product_of_digits)
"""Extract digits from strings and find the product of all digits. """
from functools import reduce

def extract_digits(ele):
    digits = ''
    for char in ele:
        if char.isdigit():
            digits += char
    return digits
li = ['a1b2', '3c4d', 'e5f6']
digit_lists = list(map(extract_digits, li))
print(digit_lists)
all_digits = [int(d) for item in digit_lists for d in item]
product_of_digits = reduce(lambda x, y: x * y, all_digits, 1)
print(product_of_digits)
"""Extract all digits and find the maximum digit using reduce."""
from functools import reduce
def max_digits(ele):
    ans = ''
    for char in ele:
        if char.isdigit():
            ans += char
    return ans
def is_valid(ele):
    if ele !='':
        return True
    else:
        return False
li = ['a7b', '39x', 'hello4', '2']
digit_strings = list(filter(is_valid, map(max_digits, li)))
print(digit_strings)
numbers = list(map(int, digit_strings))
print(numbers)
max_number = reduce(lambda x, y: x if x > y else y, numbers)
print([max_number]) 
"""Consider only strings that start with a digit. Extract digits and find the sum."""
from functools import reduce
def start_digit(ele):
    return ele[0].isdigit()
def extract_digits(ele):
    ans = ''
    for char in ele:
        if char.isdigit():
            ans += char
    return ans
li = ['1ab2', 'abc3', '4xy5', 'hello', '9z']
valid_strings = list(filter(start_digit, li))
digit_strings = list(map(extract_digits, valid_strings))
numbers = list(map(int, digit_strings))
total_sum = reduce(lambda x, y: x + y, numbers, 0)
print(valid_strings)
print(digit_strings)
print(numbers)
print(total_sum)
"""Extract digits, convert them into integers, and find the average using reduce """
from functools import reduce
def extract_digits(ele):
    ans = ''
    for char in ele:
        if char.isdigit():
            ans += char
    return ans
li = ['a10', 'b20', '30c']
digit_strings = list(map(extract_digits, li))
numbers = list(map(int, digit_strings))
Average = reduce(lambda x,y:x+y,numbers,0)/len(numbers)
print(digit_strings)
print(numbers)
print(Average)
"""Extract digits, keep digits greater than 5, and find the sum."""
from functools import reduce
def extract_digits(ele):
    ans = ''
    for char in ele:
        if char.isdigit() and int(char)>5:
            ans += char
    return ans
li = ['a1b6', '7x3', 'hello9']
digit_strings = list(map(extract_digits, li))
numbers = list(map(int, digit_strings))
total_sum = reduce(lambda x,y:x+y,numbers,0)
print(digit_strings)
print(numbers)
print(total_sum)
"""For each string, find the sum of its digits and store it in a list."""
from functools import reduce
def sum_of_digits(ele):
    ans = ''
    for char in ele:
        if char.isdigit():
            ans += char
    return ans
def is_valid(ele):
    if ele !='':
        return True
    else:
        return False
li = ['a1b2', '3x4', 'hello']
digit_strings = list(map(sum_of_digits, li))
digit_strings = list(filter(is_valid, digit_strings))   
numbers = list(map(int, digit_strings))
total_sum = list(map(lambda n: reduce(lambda x, y: x + y, map(int, str(n)), 0), numbers))
print(digit_strings)
print(numbers)
print(total_sum)
"""Extract digits from each string and identify the string with the maximum digit sum."""
from functools import reduce
def extract_digits(ele):
    ans = ''
    for char in ele:
        if char.isdigit():
            ans += char
    return ans
def is_valid(ele):
    if ele !='':
        return True
    else:
        return False
li = ['a12', '9x8', 'hello7']
digit_strings = list(filter(is_valid, map(extract_digits, li)))
print(digit_strings)
numbers = list(map(int, digit_strings))
print(numbers)
digit_sums = list(map(lambda n: reduce(lambda x, y: x + y, map(int, str(n)), 0), numbers))
print(digit_sums)