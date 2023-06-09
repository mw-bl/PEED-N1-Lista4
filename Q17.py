def filtrarStrings(listaStrings):
    novaLista = [string for string in listaStrings if len(string) > 5]
    return novaLista

entrada = input("Digite uma lista de strings separadas por espaço: ")

listaStrings = entrada.split()

resultado = filtrarStrings(listaStrings)

print("Strings com mais de 5 caracteres:", resultado)
