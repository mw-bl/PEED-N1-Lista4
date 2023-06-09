def criar_lista_nomes():
    nomes = [] 

    while True:
        nome = input("Digite um nome (ou 'sair' para encerrar e exibir a lista): ")
        if nome.lower() == "sair":
            break  
        nomes.append(nome) 

    return nomes

lista_nomes = criar_lista_nomes()
print("Lista de nomes:", lista_nomes)
