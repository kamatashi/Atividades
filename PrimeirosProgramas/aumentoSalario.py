salario = float(input())
perAumento = float(input())
novoSalario = salario + (salario * (perAumento/100))

print(f'Seu salário teve aumento de {perAumento:.1f}, passando de R$ {salario:.1f} para R$ {novoSalario:.1f}')
