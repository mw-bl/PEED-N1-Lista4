class FilaCirc:
    def _init_(self, capacidade):
        self.capacidade = capacidade
        self.fila = [None] * capacidade
        self.inicio = 0
        self.fim = 0
        self.tamanho = 0

    def is_empty(self):
        return self.tamanho == 0

    def is_full(self):
        return self.tamanho == self.capacidade

    def enfileirar(self, valor):
        if self.is_full():
            print("Fila cheia! Impossivel enfileirar.")
            return
        self.fila[self.fim] = valor
        self.fim = (self.fim + 1) % self.capacidade
        self.tamanho += 1

    def desenfileirar(self):
        if self.is_empty():
            print("Fila vazia! Impossivel desenfileirar.")
            return None
        valor = self.fila[self.inicio]
        self.fila[self.inicio] = None
        self.inicio = (self.inicio + 1) % self.capacidade
        self.tamanho -= 1
        return valor

    def exibir_fila(self):
        if self.is_empty():
            print("A fila está vazia.")
            return
        posicao = self.inicio
        elementos = []
        for i in range(self.tamanho):
            elementos.append(str(self.fila[posicao]))
            posicao = (posicao + 1) % self.capacidade
        print("Fila:", " ".join(elementos))

fila = FilaCirc(5)

fila.enfileirar(10)
fila.enfileirar(20)
fila.enfileirar(30)
fila.enfileirar(40)

fila.exibir_fila()

fila.desenfileirar()

fila.exibir_fila()

fila.enfileirar(50)
fila.enfileirar(60)

fila.exibir_fila()
