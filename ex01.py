# + 0.2

from mip import *

# cria modelo
model = Model(name="exemplo1",sense=MAXIMIZE, solver_name=CBC)

# variáveis
x1 = model.add_var(name='x1', var_type=CONTINUOUS, lb=0)
x2 = model.add_var(name='x2', var_type=CONTINUOUS, lb=0)

# restrições
model.add_constr(x1 + x2 <= 4, name='rest1')
model.add_constr(x2 <= 3.5, name='rest1')
# função objetivo
model.objective = maximize(x1 + 2*x2)

# otimiza
model.optimize()

# saida
print("sol = ", model.objective_value)