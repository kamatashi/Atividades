def criarMatrizes(matriz, numMatriz,numLinhas,numFilasInto=1):
    matriz = [[numMatriz] * numFilasInto] * numLinhas
    return matriz


matriz = []


print(criarMatrizes(matriz,[6,4],3,3))
