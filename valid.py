"""check the given string valid parentheses or not """
def valid(s):
    list = []
    m = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in m:
            top_element = list.pop() if list else "the stack is empty"
            if m[char] != top_element:
                return False
        else:
            list.append(char)
    return not list
print(valid("({[]})"))
print(valid("({[}])"))