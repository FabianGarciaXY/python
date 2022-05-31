
edad = -7

# Concatenacion de operadores en condición
if 0 < edad < 100:
    print('La edad es correcta')
else:
    print('La edad es incorrecta')

salario_p = int(input("Introduce el salario del p: "))
print(f"Salario del presidente es {salario_p}" )

salario_d = int(input("Introduce el salario del p: "))
print(f"Salario del presidente es {salario_d}" )

salario_j = int(input("Introduce el salario del p: "))
print(f"Salario del presidente es {salario_j}" )

salario_a = int(input("Introduce el salario del p: "))
print(f"Salario del presidente es {salario_a}" )

if salario_a < salario_j < salario_d < salario_p:
    print('Ok')
else:
    print('NoK')