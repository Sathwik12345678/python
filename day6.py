num=int(input())
for row in range(1,num+1):
  start = 0
  for first in range(num-row):
    print(start,end=' ')
    start = 1 if start == 0 else 0
  for second in range(row):
    print(int(not(row%2)),end=' ')
  print() 

char = input()
"""if given upper case letter convert it to lower case if given lower case it should be lower case itself"""
if 'A'<=char<='Z':
  char += 32
print(chr(ord(char)))

mask = 32
char = input() [0]
char = chr(ord(char) | mask)
print(char)
