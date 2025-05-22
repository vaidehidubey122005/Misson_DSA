def luckBalance(k, contests):
    # Separate important and unimportant contests
    important = []
    unimportant_luck = 0
    
    for luck, importance in contests:
        if importance == 1:
            important.append(luck)
        else:
            unimportant_luck += luck
    
    # Sort important contests by luck in descending order
    important.sort(reverse=True)
    
    # Maximize luck: lose the k most lucky important contests
    max_luck = unimportant_luck  # Add luck from unimportant contests
    
    for i in range(k):
        if i < len(important):
            max_luck += important[i]  # Add luck for the lost important contests
    
    # Subtract luck for the remaining important contests that we have to win
    for i in range(k, len(important)):
        if i < len(important):
            max_luck -= important[i]  # Subtract luck for the won important contests
    
    return max_luck
