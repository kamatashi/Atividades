salario = float(input())
perAumento = float(input())
novoSalario = salario + (salario * (perAumento/100))

print('Seu salário teve aumento de %.1f%%, passando de R$ %.1f para R$ %.1f' % (perAumento, salario, novoSalario))
