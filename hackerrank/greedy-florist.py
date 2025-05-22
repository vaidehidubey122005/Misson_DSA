def getMinimumCost(k, c):
    # Sort flower costs in descending order
    c.sort(reverse=True)

    # To track the number of flowers each person buys
    friends = [0] * k
    total_cost = 0
    # Go through each flower cost and assign it to a person
    for i in range(len(c)):
        person = i % k  # Find out which person is buying the flower
        # The number of flowers this person has bought increases
        total_cost += (friends[person] + 1) * c[i]
        # Increase the flower count for the person
        friends[person] += 1
    
    return total_cost
