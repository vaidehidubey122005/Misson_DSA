def fairRations(b):
    total_loaves = sum(b)
    n = len(b)

    # If the total number of loaves is not divisible by n, return -1
    if total_loaves % n != 0:
        return -1

    # Calculate the target number of loaves each person should have
    target = total_loaves // n
    operations = 0

    # Iterate through the list and try to balance the loaves
    for i in range(n - 1):
        # Calculate the difference between the current number of loaves and the target
        diff = b[i] - target
        
        # Add the absolute difference to the operations count
        operations += abs(diff)
        
        # Transfer the difference to the next person
        b[i] -= diff
        b[i + 1] += diff

    return operations
