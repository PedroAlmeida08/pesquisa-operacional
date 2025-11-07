# + 0.2

from mip import *

# cria modelo
model = Model(name="exercicio4",sense=MAXIMIZE, solver_name=CBC)

# variáveis
n = 6
x = [model.add_var(name='x_'+str(i), var_type=BINARY) for i in range(n)]

# restrições
model.add_constr(700*x[0] + 1080*x[1] + 120*x[2] + 300*x[3] + 680*x[4] + 420*x[5] <= 2000, name='rest1')
model.add_constr(6*x[0] + 16*x[1] + 2*x[2] + 4*x[3] + 10*x[4] + 6*x[5] <= 24, name='rest1')
model.add_constr(200*x[0] + 300*x[1] + 20*x[2] + 70*x[3] + 150*x[4] + 90*x[5] >= 200, name='rest1')
model.add_constr(x[2] + x[3] <= 1)
model.add_constr(x[0] <= x[5])
# função objetivo
model.objective = maximize(300*x[0] + 440*x[1] + 60*x[2] + 160*x[3] + 380*x[4] + 200*x[5])

# otimiza
model.optimize()

# saida
print("sol = ", model.objective_value)

print((x[0].x + x[1].x + x[2].x) * x[3].x * (x[4].x * x[5].x))