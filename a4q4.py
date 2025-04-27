import pulp as p
prob = p.LpProblem("Big M Method ",p.LpMinimize)
A=p.LpVariable("Food A = ",lowBound=0)
B=p.LpVariable("Food B = ",lowBound=0)
M=1e6
artifical1= p.LpVariable("Artificial1=",lowBound=0)
artifical2= p.LpVariable("Artificial2=",lowBound=0)
artifical3= p.LpVariable("Artifical3=",lowBound=0)

prob+=4*A+3*B+M*(artifical1+artifical2+artifical3)
prob+=200*A+100*B+artifical1>=4000
prob+=1*A+2*B+artifical2>=50
prob+=40*A+40*B+artifical3>=1400

print(prob)
status = prob.solve()
print(p.LpStatus[status])
print("Food A = ",p.value(A))
print("Food B = ",p.value(B))
print("Minimum cost = ",p.value(prob.objective))