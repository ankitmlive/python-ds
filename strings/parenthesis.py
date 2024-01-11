"""
create a function to check valid parenthesis.
(){}[] - valid
[{(()}] - invalid
Algo: Create a hashmap of closing and openeing bracket beacause these are fixed,
      Take a stack, we will push each opening bracket to stack and for closing bracket, we will check in stack for it's corresponding opening bracket.
      and if the last element in stack is corresponding to the bracket we are checking, we will remove the bracket(oppening) from stack.
      If stack is empty in last, parenthesis are valid otherwise not.
"""

strr = "[]{}()"

def valid(strr):
    hashed = {")":"(", "}":"{", "]":"["}
    stack = []
    for s in strr:
        if s in hashed:
            if stack and stack[-1] == hashed[s]:
                stack.pop()
            else:
                return False
        else:
            stack.append(s)
    
    return True if len(stack) == 0 else False
