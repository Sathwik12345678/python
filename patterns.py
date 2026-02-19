"""1.pattern one nxn square using * """
n=5
for row in range(1,n+1):
  for col in range(1,n+1):
    print('*',end = ' ')
  print()
print("-------------------------------------------------------------------------------")
"""2.right angle triangle"""
for row in range(1,n+1):
  for col in range(1,row+1):
    print('*',end=' ')
  print()
print("-------------------------------------------------------------------------------")
"""inverse right angle triangle"""
for row in range(n,0,-1):
  for col in range(1,row+1):
    print('*',end= ' ')
  print()
print("-------------------------------------------------------------------------------")
"""mirror right angle triangle """
for row in range(1,n+1):
  for spaces in range(n-row):
    print(' ',end=' ')
  for col in range(1,row+1):
    print('*',end=' ')
  print()
print("-------------------------------------------------------------------------------")
"""inverse of mirror right angle triangle"""
for row in range(n,0,-1):
  for spaces in range(n-row):
    print(' ',end=' ')
  for col in range(1,row+1):
    print('*',end=' ')
  print()
print("-------------------------------------------------------------------------------")
"""equilateral triangle"""
for row in range(1,n+1):
  for col in range(n,0,-1):
    if row >= col:
      print('*',end=' ')
    else:
      print(' ',end='')
  print()
"""inverse of an equilateral triangle"""
print("-------------------------------------------------------------------------------")
for row in range(n,0,-1):
  for col in range(n,0,-1):
    if row >= col:
      print('*',end=' ')
    else:
      print(' ',end='')
  print()
print("-------------------------------------------------------------------------------")
"""only odd number of stars for equilateral triangle"""
for row in range(1, n+1):
    for space in range(n - row):
        print(' ', end='')
    for col in range(2*row - 1):
        print('*', end='')
    print()
print("-------------------------------------------------------------------------------")
"""inverse of the only odd number of stars for equilateral triangle"""
for row in range(n,0,-1):
    for space in range(n - row):
        print(' ', end='')
    for col in range(2*row - 1):
        print('*', end='')
    print()
print("-------------------------------------------------------------------------------")
n = 4
total_rows = 2*n - 1
for row in range(1, total_rows + 1):
    if row <= n:
        count = row
    else:
        count = total_rows - row + 1
    print('*', end='')
    for col in range(2, count + 1):
        print('  *', end='')
    print()
print("----------------------------------------------------------------------------------------------------")
"""* and number mix pattern """
n=5
for x in range(1,n+1):
  for y in range(1,n+1):
    if y > x:
      print('*',end=' ')
    else:
      print(x,end=' ')
  print()
print("----------------------------------------------------------------------------------------------------")
""" * and number mix pattern """
n=5
for x in range(1,n+1):
  for y in range(1,n+1):
    if y > x:
      print('*',end=' ')
    else:
      print(y,end=' ')
  print()
""" * and number mix pattern  """
print("----------------------------------------------------------------------------------------------------")
n=5
for x in range(n,0,-1):
  for y in range(1,n+1):
    if y > x:
      print('*',end=' ')
    else:
      print(x,end=' ')
  print()