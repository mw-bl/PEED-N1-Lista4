import time

class Fila:
    def __init__(self):
        self.fila = []

    def adicionar(self, item):
        self.fila.append(item)
        print(f"Cliente {item} adicionado à fila.")

    def remover(self):
        if self.vazia():
            print("A fila está vazia. Não há clientes para atender.")
        else:
            cliente_atendido = self.fila.pop(0)
            print(f"Cliente {cliente_atendido} está sendo atendido.")

    def vazia(self):
        return len(self.fila) == 0

supermercado = Fila()

supermercado.adicionar(1)
time.sleep(5)
supermercado.adicionar(2)
time.sleep(5)
supermercado.adicionar(3)

for hora in range(3):
    print(f"\nHora {hora+1}:")
    supermercado.remover()
    time.sleep(5)
