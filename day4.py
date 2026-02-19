"""Patterns"""
print('*')
print('{0}'.format('*'))
print(f'{"*"}')
""" write a program to print ten stars in single line""" 
for _ in range(10):#underscore is used instead of i because we are not using i in the loop
    print('*',end=' ')
"""for printing 10*10 star pattern"""
n = int(input())
for row in range(n):
    for col in range(n):
        print("*",end=' ')
    print()
"""for printing hollow square pattern"""
n = int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        if row == 1 or col == 1 or col == n or row == n:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
"""for this pattern: """"""   * * * * 
    * * * * 
  * * * * 
* * * * """
n = int(input())
for row in range(1,n+1):
    for spaces in range(1,n-row+1):
        print(' ',end=' ')
    for col in range(1,n+1):
        print("*",end=' ')
    print()

""" for left tilt on above question"""
n = int(input())
for row in range(1,n+1):
    for spaces in range(row-1):
        print(' ',end=' ')
    for col in range(1,n+1):
        print("*",end=' ')
    print()
"""hallow at middle for the above pattern"""
n = int(input())
for row in range(1,n+1):
    for spaces in range(n-row):
        print(' ',end=' ')
    for col in range(1,n+1):
        if row == 1 or col == 1 or col == n or row == n:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
"""for left tilt"""
n = int(input())
for row in range(1,n+1):
    for spaces in range(row-1):
        print(' ',end=' ')
    for col in range(1,n+1):
        if row == 1 or col == 1 or col == n or row == n:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
"""for a matrix with * pattern"""
n = int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        print('*',end=' ')
    print()
"""for a right angle triangle """
n = int(input())
for row in range(1,n+1):
    for col in range(1,row+1):
        print('*',end=' ')
    print()
"""for a hollow right angle triangle"""
n = int(input())
for row in range(1,n+1):
    for col in range(1,row+1):
        if col == 1 or row == n or row == col:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
"""right tilted right angle triangle"""
n = int(input())
for row in range(1,n+1):
    for spaces in range(n-row):
        print(' ',end=' ')
    for col in range(1,row+1):
        print('*',end=' ')
    print()
"""inverse or mirror right angle triangle"""
n = int(input())
for row in range(n,0,-1):
    for col in range(1,row+1):
            print('*',end=' ')
    print()
"""inverted hallow"""
n = int(input())
for row in range(n,0,-1):
    for col in range(1,row+1):
        if col == 1 or row == n or row == col:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
"""mirror of already inverted triangle"""
n = int(input())
for row in range(n,0,-1):
    for spaces in range(n-row):
        print(' ',end=' ')
    for col in range(1,row+1):
            print('*',end=' ')
    print()
"""hallow mirror of inverted triangle"""
n = int(input())
for row in range(n,0,-1):
    for spaces in range(n-row):
        print(' ',end=' ')
    for col in range(1,row+1):
        if col == 1 or row == n or row == col:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()