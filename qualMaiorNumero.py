def maiorNumero(lista):
    numero = 0

    for i in lista:
        if numero < i:
            numero = i
    
    return numero