import numpy as np

# Function to implement Least Cost Method for transportation problem
def least_cost_method(cost, supply, demand):
    # Create an allocation matrix to store the allocation of goods
    allocation = np.zeros_like(cost)

    # While there is supply or demand left
    while np.sum(supply) > 0 and np.sum(demand) > 0:
        # Find the least cost cell in the cost matrix
        min_cost_index = np.unravel_index(np.argmin(cost), cost.shape)
        i, j = min_cost_index
        
        # Find the quantity that can be transported, which is the min of supply and demand
        transport_quantity = min(supply[i], demand[j])

        # Allocate goods from source i to destination j
        allocation[i, j] = transport_quantity

        # Update the supply and demand
        supply[i] -= transport_quantity
        demand[j] -= transport_quantity

        

    return allocation

# Function to calculate the total transportation cost
def total_cost(cost, allocation):
    return np.sum(cost * allocation)

# Example cost matrix (cost to transport goods from sources to destinations)
cost = np.array([
    [4, 3, 1, 2, 6],  # Cost from source 1 to destinations 1, 2, 3, 4, 5
    [5, 2, 3, 4, 5],  # Cost from source 2 to destinations 1, 2, 3, 4, 5
    [3, 5, 6, 3, 2],  # Cost from source 3 to destinations 1, 2, 3, 4, 5
    [2, 4, 4, 5, 3]   # Cost from source 4 to destinations 1, 2, 3, 4, 5
])

# Supply available at each source
supply = np.array([80, 60, 40, 20])

# Demand at each destination
demand = np.array([60, 60, 30, 40, 10])

# Apply the Least Cost Method to solve the problem
allocation = least_cost_method(cost.copy(), supply.copy(), demand.copy())

# Calculate the total transportation cost
cost_result = total_cost(cost, allocation)

# Print the allocation and total cost
print("Allocation Matrix (Goods Allocated from Sources to Destinations):")
print(allocation)

print("\nTotal Transportation Cost:")
print(cost_result)
