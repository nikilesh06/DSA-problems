def validParanthes(s):
    
    stack =[]
    for char in s:
        if char == '(':
            stack.append(')')
        elif char == '[':
            stack.append(']')
        elif char == '{':
            stack.append('}')
        elif stack == [] or stack.pop() != char:
            return False
    return True if stack == [] else False

st = "{()}"
print(validParanthes(st))