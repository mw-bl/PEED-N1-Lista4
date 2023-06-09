def encontrarPalavraMaisLonga(listaPalavras):
    palavraMaisLonga = ""
    for palavra in listaPalavras:
        if len(palavra) > len(palavraMaisLonga):
            palavraMaisLonga = palavra
    return palavraMaisLonga

entrada = input("Digite uma lista de palavras separadas por espaço: ")

listaPalavras = entrada.split()

resultado = encontrarPalavraMaisLonga(listaPalavras)

print("A palavra mais longa é:", resultado)
