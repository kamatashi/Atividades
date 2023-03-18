# Faça um programa para determinar se 2 números primos (X e Y) somados resultam em outro número primo.


def toInt(lista):
	for i in lista:
		int(i)

numes = [nume1, nume2] = int(input())

toInt(numes)

def ePrimo(numero):
	if numero > 1:
		for i in range(2, numero):
			if numero % i == 0:
				print('O numero {} nao eh primo.'.format(numero))
				return False
		else:
			return True

def somaPrimos(numero1, numero2):
	if ePrimo(numero1) and ePrimo(numero2):
		return 'A soma de {} e {} eh um primo.'.format(numero1, numero2)
	else:
		return 'A soma de {} e {} nao eh um primo.'.format(numero1, numero2)


