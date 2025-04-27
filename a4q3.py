import matplotlib.pyplot as plt
from scipy.optimize import linprog
import numpy as np

c = [-12,-15,-14]
A = [
    [1,1,1],
    [-0.01,0.01,0],
    [0,-1,2]
]
b = [100,0,0]

x_bounds=(0,None)

res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds]*3, method='highs')

print(f"Optimal solution : ")
print(f"Coal A : {res.x[0]:.2f} Tons")
print(f"Coal B : {res.x[1]:.2f} Tons")
print(f"Coal C : {res.x[2]:.2f} Tons")
print(f"Maximum profit : {-res.fun:.2f} BDT")

