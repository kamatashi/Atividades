def ordenador(lista):
    for i in range(len(lista)-1):
        j = indiceDoMenor(i, lista)
        lista[i], lista[j] = lista[j], lista[i]
    
    return lista



def indiceDoMenor(i, lista):
    # Usamos um apoio de indíce para guardar as váriaveis que são menores
    apoio = i

    for k in range(apoio+1, len(lista)):
        if lista[apoio] > lista[i]:
            apoio = k
        
    return apoio


lista = [1,4,57,8,7,4,2,133,1,3]
print(ordenador(lista))
