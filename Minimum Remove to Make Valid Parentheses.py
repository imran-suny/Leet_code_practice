def minRemoveToMakeValid(s: str) -> str:
    # First pass: Remove invalid closing parentheses
    s_list = list(s)
    stack = []
    
    for i in range(len(s_list)):
        if s_list[i] == '(':
            # Store the index of the opening parenthesis
            stack.append(i)
        elif s_list[i] == ')':
            # If there's an unmatched closing parenthesis, mark it for removal
            if stack:
                stack.pop()  # Matched opening parenthesis, so pop from stack
            else:
                s_list[i] = ''  # Invalid closing parenthesis, mark it as empty
    
    # Second pass: Remove unmatched opening parentheses
    while stack:
        s_list[stack.pop()] = ''  # Mark unmatched opening parenthesis as empty
    
    # Join the list back into a string and return the result
    return ''.join(s_list)

# Example usage:
s = "lee(t(c)o)de)"
print(minRemoveToMakeValid(s))  # Output: "lee(t(c)o)de"
