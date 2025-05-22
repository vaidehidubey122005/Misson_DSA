def manasaAndStones(n, a, b):
    # Use a set to store the distinct sums
    distinct_sums = set()

    # Calculate all possible sums
    for x in range(n):
        # Calculate the sum for x stones of type a and (n-x) stones of type b
        sum_value = x * a + (n - x - 1) * b
        distinct_sums.add(sum_value)
    
    # Return the sorted list of distinct sums
    return sorted(distinct_sums)

# Example input
n = 3
a = 1
b = 2

# Output the distinct sums
print(manasaAndStones(n, a, b))
