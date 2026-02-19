"""pattern printing """
n = 9
for row in range(1,n+1):
    for col in range(1,n+1):
        if row == 1 or col == 1 or col == n or row == n:
            print("*",end=' ')
        elif row == col or row +col == n+1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print() 
print("-------------------------------------------------------------")
""" 2. pattern"""
for row in range(1,n+1):
    for col in range(2*row-1):
        print('*',end=' ')
    print()
print("-------------------------------------------------------------")
"""3.equilateral triangle"""
for row in range(1,n+1):
    for space in range(n-row):
        print(' ',end=' ')
    for col in range(2*row-1):
        print('*',end=' ')
    print()
print("-------------------------------------------------------------")
"""inverse of it"""
for row in range(n,0,-1):
    for spaces in range(n-row):
        print(' ',end=' ')
    for col in range(2*row-1):
        print('*',end=' ')
    print()
print("-------------------------------------------------------------")
"""rhombus"""
for row in range(1,n):
    for space in range(n-row):
        print(' ',end=' ')
    for col in range(2*row-1):
        print('*',end=' ')
    print()
for row in range(n,0,-1):
    for spaces in range(n-row):
        print(' ',end=' ')
    for col in range(2*row-1):
        print('*',end=' ')
    print()
print("-------------------------------------------------------------")
"""hour glass"""
for row in range(n,1,-1):
    for spaces in range(n-row):
        print(' ',end=' ')
    for col in range(2*row-1):
        print('*',end=' ')
    print()
for row in range(1,n+1):
    for space in range(n-row):
        print(' ',end=' ')
    for col in range(2*row-1):
        print('*',end=' ')
    print()
print("-------------------------------------------------------------")
"""hallow rhombus"""
for row in range(1,n):
    for space in range(n-row):
        print(' ',end=' ')
    for col in range(1,2*row):
        if col == 2*row-1 or col==1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
for row in range(n,0,-1):
    for spaces in range(n-row):
        print(' ',end=' ')
    for col in range(1,2*row):
        if col == 2*row-1 or col==1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
""" hallow rhombus inside a square """
print("-------------------------------------------------------------")
n = 9
for row in range(n,1,-1):
    for col in range(1,row+1):
        print('*',end=' ')
    for spaces in range(2*(n-row)):
        print(' ',end=' ')
    for col in range(1,row+1):
        print('*',end=' ')
    print()
#bottom
for row in range(1,n+1):
    for col in range(1,row+1):
        print('*',end=' ')
    for spaces in range(2*(n-row)):
        print(' ',end=' ')
    for col in range(1,row+1):
        print('*',end=' ')
    print()
print("-------------------------------------------------------------")
"""patterns"""
for row in range(n):
    for col in range(n):
        if row%2==0 and col%2==0:
            print('*',end=' ')
        elif row%2==1 and col%2==1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
print("-------------------------------------------------------------")
"""or"""
for row in range(n):
    for col in range(n):
        if (row+col)%2==0:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
print("-------------------------------------------------------------")
"""number square pattern"""
n=5
for row in range(1,n+1):
    for col in range(n):
        print(row,end=' ')
    print()
print("-------------------------------------------------------------")
n=5
start = None
for row in range(1,n+1):
    start = 2 if row%2==0 else 1
    for col in range(1,row+1):
        print(start,end=' ')
        start += 2
    print()
print("--------------------------------------------------------------")
n=5
for row in range(1,n):
    for space in range(n-row):
        print(' ',end=' ')
    for col in range(2*row-1):
        print(row,end=' ')
    print()
for row in range(n,0,-1):
    for spaces in range(n-row):
        print(' ',end=' ')
    for col in range(2*row-1):
        print(row,end=' ')
    print()
print("--------------------------------------------------------------")
for row in range(n,1,-1):
    for spaces in range(n-row):
        print(' ',end=' ')
    for col in range(2*row-1):
        print(row,end=' ')
    print()
for row in range(1,n+1):
    for space in range(n-row):
        print(' ',end=' ')
    for col in range(2*row-1):
        print(row,end=' ')
    print()
print("--------------------------------------------------------------")
for row in range(n,1,-1):
    for front in range(n,row,-1):
        print(front,end=' ')
    for col in range(2*row-1):
        print(row,end=' ')
    for lag in range(row+1,n+1):
        print(lag,end=' ')
    print()
for row in range(1,n+1):
    for front in range(n,row,-1):
        print(front,end=' ')
    for col in range(2*row-1):
        print(row,end=' ')
    for lag in range(row+1,n+1):
        print(lag,end=' ')
    print()