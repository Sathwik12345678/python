""" Bitwise exclusiveOR & XOR  used for inverting the state of a bit
"""
"""given a character invert its case using """
"""solution 1"""
char = input() [0]
if 'A' <= char <= 'Z':
  char = chr(ord(char) + 32)
else:
  char = chr(ord(char) - 32)
print(char)
print("-------------------------------------------------------")
"""solution 2 XOR is also known as """
char = input() 
char = chr(ord(char) ^ 32)
print(char)
print("-------------------------------------------------------")
"""left shift operator << used for moving active bits from lower 
2 powers to higher 2 powers (to the left) by mentioned many bits
Notes: works in the same manner for both positive and negative values
can be used for multiplying in terms of two
left shift means (A<<B = A*2^B) 
"""
"""given a number find the number of active bits in the binary representation of the value using bitwise operator using left shift and and operator"""
num = int(input())
mask = 1
count = 0
while mask <= num:
  if num & mask != 0:
    count += 1
  mask <<= 1
print(count)
print("-------------------------------------------------------")
"""find the in active bits"""
num = int(input())
mask = 1
count = 0
while mask <= num:
  if not (num & mask):
    count += 1
  mask <<= 1
print(count)
"""negative representation of a number using left shift operator"""
"""negative values are stored 
as two's complement 2's complement = 1's complement+1 1's complement can be obtained by
inverting the state of all the bits of the value"""

"""negation or inversion """

"""given integer number find the number of trailing zeros in the factorial representation of the number """
num = int(input())
"""first calculate the factorial of the number"""
num = int(input())
"""first calculate the factorial of the number"""
fact = 1
for i in range(2, num + 1):
  fact *= i
print(fact)
""" now trailing zeros"""
count = 0
for i in range(fact):
  if fact % 10 == 0:
    count+=1
    fact //= 10
  else:
    break
print(count)
""" using optimized solution """
num = int(input())
count = 0
div = 5
while div <= num:
    count +=(num//div)
    div *= 5
print(count)
"""prime factorization of a number"""
num = int(input())
factors = []

for i in range(2, num + 1):
    while num % i == 0:
        factors.append(i)
        num //= i
    if num == 1:
        break

print(factors)


"""now using bitwise"""
num = int(input())
factors = []
for i in range(2, num + 1):
  num &= ~(i-1) # clear the bits below i
  while num % i == 0:
    factors.append(i)
    num //= i
  if num == 1:
    break
print(factors)