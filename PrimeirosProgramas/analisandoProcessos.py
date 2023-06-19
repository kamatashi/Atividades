# Betina trabalha em um escritório de advocacia e todos os dias analisa vários processos. Sabendo que ela cumpre um expediente diário de 8h, escreva um programa que receba como entrada quantos minutos ela leva para analisar cada processo, e exiba o total de processos revisados em um dia de trabalho. (Dica: Uma hora tem 60 minutos)
# Essa resposta não foi pensada por mim. Analise como funciona a lógica!
tempoProcessosMin = int(input())

expediente = 8

processosDia = (expediente * 60) // tempoProcessosMin

print(processosDia)
