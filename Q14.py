class No:
    def __init__(self, dado):
        self.dado = dado
        self.prox = None


class ListaEncadeadaCircular:
    def __init__(self):
        self.head = None

    def estaVazia(self):
        return self.head is None

    def inserirEmOrdem(self, dado):
        novoNo = No(dado)
        if self.estaVazia():
            novoNo.prox = novoNo 
            self.head = novoNo
        elif dado <= self.head.dado:
            novoNo.prox = self.head
            atual = self.head
            while atual.prox != self.head:
                atual = atual.prox
            atual.prox = novoNo
            self.head = novoNo
        else:
            atual = self.head
            while atual.prox != self.head and atual.prox.dado < dado:
                atual = atual.prox
            novoNo.prox = atual.prox
            atual.prox = novoNo

    def mostrarPrimeiro(self):
        if self.estaVazia():
            print("A lista está vazia.")
        else:
            print("Primeiro elemento:", self.head.dado)

    def mostrarUltimo(self):
        if self.estaVazia():
            print("A lista está vazia.")
        else:
            atual = self.head
            while atual.prox != self.head:
                atual = atual.prox
            print("Último elemento:", atual.dado)


def main():
    lista = ListaEncadeadaCircular()

    numeros = input("Digite uma lista de números inteiros (separados por espaço): ").split()

    for numero in numeros:
        lista.inserirEmOrdem(int(numero))

    lista.mostrarPrimeiro()
    lista.mostrarUltimo()


if __name__ == "__main__":
    main()
