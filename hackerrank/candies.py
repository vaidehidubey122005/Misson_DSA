def candy(ratings):
    n = len(ratings)
    if n == 0:
        return 0
    
    # Step 1: Initialize the candies array with 1 candy for each child.
    candies = [1] * n
    
    # Step 2: Left to right pass
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1
    
    # Step 3: Right to left pass
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)
    
    # Step 4: The total candies is the sum of all elements in the candies array.
    return sum(candies)
