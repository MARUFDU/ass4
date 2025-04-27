import numpy as np

def least_cost_method(supply, demand, cost):
    # Initialize the transportation matrix with zeros
    transport_matrix = np.zeros((len(supply), len(demand)))
    
    # Copy the supply and demand values to avoid modifying original lists
    supply = supply.copy()
    demand = demand.copy()
    
    # Continue allocating units until all supply and demand are exhausted
    while np.sum(supply) > 0 and np.sum(demand) > 0:
        # Find the cell with the minimum cost
        min_cost_idx = np.unravel_index(np.argmin(cost), cost.shape)
        i, j = min_cost_idx
        
        # Allocate the minimum of available supply and demand to the current cell
        allocation = min(supply[i], demand[j])
        transport_matrix[i][j] = allocation
        
        # Update the supply and demand
        supply[i] -= allocation
        demand[j] -= allocation
        
        # If supply is exhausted for this row, set the cost of this row to infinity to ignore it
        if supply[i] == 0:
            cost[i, :] = np.inf  # Ignore this row in future iterations
        
        # If demand is exhausted for this column, set the cost of this column to infinity to ignore it
        if demand[j] == 0:
            cost[:, j] = np.inf  # Ignore this column in future iterations
    
    return transport_matrix

# Example supply, demand, and cost matrices
supply = [80, 60, 40, 20]  # Supply at each source
demand =  [60,60,30, 40, 10] # Demand at each destination
cost = [
    [4,3,1,2,6],  # Cost of transportation from source 1 to destinations 1, 2, 3
    [5,2,3,4,5],   # Cost of transportation from source 2 to destinations 1, 2, 3
    [3,5,6,3,2],
    [2,4,4,5,3]    # Cost of transportation from source 3 to destinations 1, 2, 3
]

# Convert the cost to a numpy array for easier manipulation
cost = np.array(cost)

# Call the Least Cost Method function
transport_matrix = least_cost_method(supply, demand, cost)

# Output the resulting transportation matrix
print("Transportation Matrix (Least Cost Method):")
print(transport_matrix)

# Calculate the total cost
total_cost = np.sum(transport_matrix * cost)
print(f"Total transportation cost: {total_cost}")
