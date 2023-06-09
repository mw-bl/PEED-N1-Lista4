def elementosComuns(lista1, lista2):
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    elementosComuns = list(conjunto1.intersection(conjunto2))
    return elementos_comuns

entrada1 = input("Digite a primeira lista de números separados por espaço: ")

lista1 = [int(numero) for numero in entrada1.split()]

entrada2 = input("Digite a segunda lista de números separados por espaço: ")

lista2 = [int(numero) for numero in entrada2.split()]

resultado = elementosComuns(lista1, lista2)

print("Elementos comuns nas duas listas:", resultado)
