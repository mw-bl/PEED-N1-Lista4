class No:
    def __init__(self, dado):
        self.dado = dado
        self.ant = None
        self.prox = None


class ListaDuplamenteEncadeada:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def estaVazia(self):
        return self.primeiro is None

    def inserirNoInicio(self, dado):
        novoNo = No(dado)
        if self.estaVazia():
            self.primeiro = novoNo
            self.ultimo = novoNo
        else:
            novoNo.prox = self.primeiro
            self.primeiro.ant = novoNo
            self.primeiro = novoNo

    def inserirNoFinal(self, dado):
        novoNo = No(dado)
        if self.estaVazia():
            self.primeiro = novoNo
            self.ultimo = novoNo
        else:
            novoNo.ant = self.ultimo
            self.ultimo.prox = novoNo
            self.ultimo = novoNo

    def removerDoInicio(self):
        if self.estaVazia():
            print("A lista está vazia.")
            return

        if self.primeiro == self.ultimo:
            self.primeiro = None
            self.ultimo = None
        else:
            self.primeiro = self.primeiro.prox
            self.primeiro.ant = None

    def removerDoFinal(self):
        if self.estaVazia():
            print("A lista está vazia.")
            return

        if self.primeiro == self.ultimo:
            self.primeiro = None
            self.ultimo = None
        else:
            self.ultimo = self.ultimo.ant
            self.ultimo.prox = None

    def exibirLista(self):
        if self.estaVazia():
            print("A lista está vazia.")
            return

        atual = self.primeiro
        while atual is not None:
            print(atual.dado, end=" ")
            atual = atual.prox
        print()


lista = ListaDuplamenteEncadeada()

lista.inserirNoInicio(3)
lista.inserirNoInicio(2)
lista.inserirNoInicio(1)

lista.inserirNoFinal(4)
lista.inserirNoFinal(5)

lista.exibirLista()

lista.removerDoInicio()

lista.removerDoFinal()

lista.exibirLista()
