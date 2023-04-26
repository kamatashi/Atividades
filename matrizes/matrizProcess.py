def matrizProcess(matriz):
  acc = len(matriz)
  while acc > 0:
    acc -= 1
    for elem in matriz:
      print(elem)


matriz = [[4, 3, 2, 5, 6, 3, 5], [3, 5, 3, 2]]

matrizProcess(matriz)
