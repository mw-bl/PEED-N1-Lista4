class No:
    def __init__(self, data):
        self.data = data
        self.next = None


class ListaEncad:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def inserirNoInicio(self, data):
        novoNo = No(data)
        novoNo.next = self.head
        self.head = novoNo

    def inserirNoFinal(self, data):
        novoNo = No(data)

        if self.is_empty():
            self.head = novoNo
            return

        atual = self.head
        while atual.next is not None:
            atual = atual.next

        atual.next = novoNo

    def removerNoInicio(self):
        if self.is_empty():
            print("A lista está vazia. Não é possível remover.")
            return

        self.head = self.head.next

    def removerNoFinal(self):
        if self.is_empty():
            print("A lista está vazia. Não é possível remover.")
            return

        if self.head.next is None:
            self.head = None
            return

        atual = self.head
        while atual.next.next is not None:
            atual = atual.next

        atual.next = None

    def display(self):
        if self.is_empty():
            print("A lista está vazia.")
            return

        atual = self.head
        while atual is not None:
            print(atual.data, end=" -> ")
            atual = atual.next
        print("None")


lista = ListaEncad()

lista.inserirNoInicio(3)
lista.inserirNoInicio(2)
lista.inserirNoInicio(1)

lista.display()  

lista.inserirNoFinal(4)
lista.inserirNoFinal(5)

lista.display() 

lista.removerNoInicio()

lista.display() 

lista.removerNoFinal()

lista.display() 
