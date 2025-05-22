def truckTour(gas, cost):
    total_fuel = 0
    current_fuel = 0
    start_index = 0
    
    for i in range(len(gas)):
        total_fuel += gas[i] - cost[i]
        current_fuel += gas[i] - cost[i]
        
        # If we can't move forward, we need to change the starting point
        if current_fuel < 0:
            start_index = i + 1
            current_fuel = 0
    
    # If total fuel is non-negative, we can complete the circuit
    if total_fuel >= 0:
        return start_index
    else:
        return -1  # Return -1 if no valid start index (not required for valid inputs)
