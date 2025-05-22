def waiter(plates, num_set):
    # Stack for final order of plates
    served = []
    
    # Stack 1 is the original plates stack
    stack1 = plates
    stack2 = []

    # For each number in num_set, process the plates and serve
    for num in num_set:
        # Move plates from stack1 to stack2, keeping only the ones equal to num in stack1
        temp_stack = []
        
        # Move plates that are not equal to num to stack2
        for plate in stack1:
            if plate == num:
                served.append(plate)  # Serve the plate
            else:
                temp_stack.append(plate)
        
        # After processing the current number, stack1 becomes temp_stack (plates not served)
        stack1 = temp_stack
    
    # Now, serve the remaining plates that are not removed
    served += stack1

    return served
