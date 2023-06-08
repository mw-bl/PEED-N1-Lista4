class Fila:
    def __init__(self):
        self.fila = []
    
    def adicionar(self, valor):
        self.fila.append(valor)
    
    def remover(self):
        if len(self.fila) > 0:
            return self.fila.pop(0)
        else:
            return None
    
    def tamanho(self):
        return len(self.fila)
    
    def mostrar(self):
        return self.fila

fila = Fila()

while True:
    print("1. Adicionar número na fila")
    print("2. Remover número da fila")
    print("3. Tamanho da fila")
    print("4. Mostrar fila")
    print("5. Sair")
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        num = int(input("Digite o número a ser adicionado: "))
        fila.adicionar(num)
    elif opcao == 2:
        removido = fila.remover()
        if removido is not None:
            print(f"O número {removido} foi removido da fila.")
        else:
            print("A fila está vazia.")
    elif opcao == 3:
        print(f"O tamanho da fila é {fila.tamanho()}.")
    elif opcao == 4:
        print(f"A fila é: {fila.mostrar()}")
    elif opcao == 5:
        break
    else:
        print("Opção inválida.")
