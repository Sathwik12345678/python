# tuple
t = (1, 2, 2, 2.1, "prasad")
print(type(t))
print(t)

# tuple indexing
t = (10, 20, 30, 40)
print(t[0])
print(t[-4])

# tuple slicing
t = (10, 20, 30, 40)
print(t[1:3])
print(t[:3])
print(t[2:3])
print(t[1:])

# concatenation operator
t1 = (1, 2, 3)
t2 = (4, 5, 6)
print(t1 + t2)

# repetition
t = (1, 2, 3)
print(t * 3)

# membership operator
t = (10, 20, 30, 40)
print(30 in t)
print(10 in t and 40 in t)

# tuple methods
# 1. count()
t = (1, 2, 2, 3, 4, 2)
print(t.count(2))

# 2. index()
t = (10, 20, 30, 40)
print(t.index(30))
