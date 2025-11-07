# Corrigir

from mip import *

# cria modelo
model = Model(name="exercicio2",sense=MINIMIZE, solver_name=CBC)

# variáveis
x = [[model.add_var(name='x_'+str(i)+'_'+str(j), var_type=INTEGER, lb=0) for j in range(3)] for i in range(2)]
for i in range (2):
    for j in range (3):
        print(x[i][j])

y1 = model.add_var(name='y1', var_type=BINARY)
y2 = model.add_var(name='y2', var_type=BINARY)

# restrições
model.add_constr(x[0][0] + x[1][0] == 120, name='rest1')
model.add_constr(x[0][1] + x[1][1]<= 3.5, name='rest1')
model.add_constr(x[0][2] + x[1][2] == 150, name='rest1')
model.add_constr(x[0][0] + x[0][1] + x[0][2] <= 200 * y1, name='rest1')
model.add_constr(x[1][0] + x[1][1] + x[1][2] <= 440 * y2, name='rest1')

# função objetivo
model.objective = minimize(2*x[0][0] + 4*x[0][1] + 5*x[0][2] + 8*x[1][0] + 6*x[1][1] + 3*x[1][2] + 3000*y1 + 7500*y2)

# otimiza
model.optimize()

# saida
print("sol = ", model.objective_value)