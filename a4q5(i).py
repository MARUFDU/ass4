import numpy as np

def northwest_corner_method(supply, demand):
    # Initialize the transportation matrix with zeros
    transport_matrix = np.zeros((len(supply), len(demand)))
    
    # Copy the supply and demand values to avoid modifying original lists
    supply = supply.copy()
    demand = demand.copy()
    
    # Starting at the top-left corner
    i, j = 0, 0
    
    while i < len(supply) and j < len(demand):
        # Allocate the minimum of supply and demand to the current cell
        allocation = min(supply[i], demand[j])
        transport_matrix[i][j] = allocation
        
        # Update the supply and demand
        supply[i] -= allocation
        demand[j] -= allocation
        
        # If supply is exhausted, move to the next row
        if supply[i] == 0:
            i += 1
        
        # If demand is exhausted, move to the next column
        if demand[j] == 0:
            j += 1
    
    return transport_matrix

# Example supply and demand arrays
supply = [80, 60, 40, 20]  # Supply at each source
demand = [60,60,30, 40, 10]  # Demand at each destination

# Call the Northwest Corner Method function
transport_matrix = northwest_corner_method(supply, demand)

# Output the resulting transportation matrix
print("Transportation Matrix (Northwest Corner Method):")
print(transport_matrix)

# Calculate the total cost (for illustration, assume cost matrix is 1 for each route)
cost = np.ones_like(transport_matrix)  # Assume cost of 1 for each unit
total_cost = np.sum(transport_matrix * cost)
print(f"Total transportation cost: {total_cost}")
