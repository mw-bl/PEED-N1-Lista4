class No:
    def __init__(self, numero):
        self.numero = numero
        self.prox = None


class Roleta:
    def __init__(self):
        self.head = None

    def estaVazia(self):
        return self.head is None

    def adicionarNumero(self, numero):
        novoNo = No(numero)
        if self.estaVazia():
            novoNo.prox = novoNo
            self.head = novoNo
        else:
            atual = self.head
            while atual.prox != self.head:
                atual = atual.prox
            atual.prox = novoNo
            novoNo.prox = self.head

    def girarRoleta(self, numeroSorteado, numeroApostado):
        if self.estaVazia():
            print("A roleta está vazia.")
            return

        atual = self.head
        while True:
            if atual.numero == numeroSorteado:
                print("Número sorteado:", numeroSorteado)
                print("Número apostado:", numeroApostado)
                if atual.numero == numeroApostado:
                    print("Você ganhou!")
                else:
                    print("Você perdeu!")
                return
            atual = atual.prox
            if atual == self.head:
                break

        print("Número sorteado:", numeroSorteado)
        print("Você perdeu!")


def main():
    roleta = Roleta()

    for numero in range(0, 37):
        roleta.adicionarNumero(numero)

    numeroApostado = int(input("Digite um número para apostar na roleta (de 0 a 36): "))

    import random

    numeroSorteado = random.randint(0, 36)
    roleta.girarRoleta(numeroSorteado, numeroApostado)


if __name__ == "__main__":
    main()
