def matrizProcess(matriz, acc=0):
  if len(matriz) == 0:
    return matriz
  else:
    acc += 1
    print('ok')
    for elem in matriz:
      print(elem)
    matrizProcess(matriz[acc], acc)


matriz = [[4, 3, 2, 5, 6, 3, 5], [3, 5, 3, 2]]

matrizProcess(matriz)
