class No:
    def __init__(self, dado):
        self.dado = dado
        self.prox = None


class ListaEncadeadaCircular:
    def __init__(self):
        self.head = None

    def estaVazia(self):
        return self.head is None

    def inserirNoInicio(self, dado):
        novoNo = No(dado)
        if self.estaVazia():
            novoNo.prox = novoNo 
        else:
            novoNo.prox = self.head
            atual = self.head
            while atual.prox != self.head:
                atual = atual.prox
            atual.prox = novoNo
        self.head = novoNo

    def inserirNoFinal(self, dado):
        novoNo = No(dado)
        if self.estaVazia():
            novoNo.prox = novoNo  
            self.head = novoNo
        else:
            atual = self.head
            while atual.prox != self.head:
                atual = atual.prox
            atual.prox = novoNo
            novoNo.prox = self.head

    def removerDoInicio(self):
        if self.estaVazia():
            print("A lista está vazia.")
            return

        atual = self.head
        while atual.prox != self.head:
            atual = atual.prox
        if atual == self.head: 
            self.head = None
        else:
            self.head = self.head.prox
            atual.prox = self.head

    def removerDoFinal(self):
        if self.estaVazia():
            print("A lista está vazia.")
            return

        atual = self.head
        prev = None
        while atual.prox != self.head:
            prev = atual
            atual = atual.prox
        if prev is None: 
            self.head = None
        else:
            prev.prox = self.head

    def exibirLista(self):
        if self.estaVazia():
            print("A lista está vazia.")
            return

        atual = self.head
        while True:
            print(atual.dado, end=" ")
            atual = atual.prox
            if atual == self.head:
                break
        print()

lista = ListaEncadeadaCircular()

lista.inserirNoInicio(3)
lista.inserirNoInicio(2)
lista.inserirNoInicio(1)

print("Lista encadeada circular:")
lista.exibirLista()

lista.inserirNoFinal(4)

print("Lista encadeada circular após inserção no final:")
lista.exibirLista()

lista.removerDoInicio()

print("Lista encadeada circular após remoção do início:")
lista.exibirLista()

lista.removerDoFinal()

print("Lista encadeada circular após remoção do final:")
lista.exibirLista()
