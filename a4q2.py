import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,400,400)
y = np.linspace(0,400,400)
X,Y = np.meshgrid(x,y)

protein_constraint = 3*X + 4*Y >= 800
fat_constraint = 2*X + 2*Y >= 200
carb_constraint = 6*X + 4*Y >= 700
non_negative = (X>=0) & (Y>=0)

feasible_region = protein_constraint & fat_constraint & carb_constraint & non_negative

Z = 45*X + 40*Y
Z_feasible = np.where(feasible_region,Z,np.inf)

min_value = np.min(Z_feasible)
min_index = np.unravel_index(np.argmin(Z_feasible),Z_feasible.shape)
min_x1 = X[min_index]
min_x2 = Y[min_index]

plt.figure(figsize=(10,8))
plt.contourf(X,Y,feasible_region,levels=[0.5,1],colors=['#ccffcc'])

plt.plot(x,(800-3*x)/4,label='Protein <= 800')
plt.plot(x,(200-2*x)/2,label='Fat <= 200')
plt.plot(x,(700-6*x)/4,label='Carbohydrate <= 700')
plt.plot(min_x1,min_x2,'ro',label=f'Min Z= {min_value:.2f} at ({min_x1:.2f},{min_x2:.2f})')

print(min_value)

plt.xlim(0,400)
plt.ylim(0,400)
plt.xlabel('Food Type 1')
plt.ylabel('Food Type 2')
plt.title('Minimising Cost')
plt.grid(True)
plt.legend()
plt.show()