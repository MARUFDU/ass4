import numpy as np
from scipy.optimize import linear_sum_assignment

profit = np.array([
    [16,10,14,11],
    [14,11,15,15],
    [15,15,13,12],
    [13,12,14,15]
])
cost = profit.max() - profit
row,col = linear_sum_assignment(cost)

salesmen = ['A','B','C','D']
cities = ['1','2','3','4']

total_cost = 0
print('Assignment : ')
for i in range(len(row)):
    print(f"Salesman {salesmen[row[i]]} to city {cities[col[i]]} (Profit : {profit[row[i],col[i]]})")

    total_cost += profit[row[i],col[i]]

print(f"\n Maximum Profit : {total_cost} BDT")