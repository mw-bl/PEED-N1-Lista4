def calcularSomaLista():
    numeros = input("Digite uma lista de números separados por espaço: ").split()
    numeros = [int(num) for num in numeros]
    soma = sum(numeros)
    return soma

resultado = calcularSomaLista()
print("A soma dos números é:", resultado)
