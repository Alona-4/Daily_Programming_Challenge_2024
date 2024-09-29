def insert_at_bottom(stack, element):
    if not stack:  
        stack.append(element)
    else:
        temp = stack.pop()
        insert_at_bottom(stack, element)
        stack.append(temp)
def reverse_stack(stack):
    if not stack:  
        return
    temp = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, temp)
stack = [3, 3, 3]
print("Original Stack:", stack)
reverse_stack(stack)
print("Reversed Stack:", stack)
