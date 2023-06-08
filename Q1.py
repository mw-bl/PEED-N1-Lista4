class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return "A fila está vazia."
        return self.queue.pop(0)

    def front(self):
        if self.is_empty():
            return "A fila está vazia."
        return self.queue[0]


fila = Queue()

numElementos = int(input("Digite o número de elementos que deseja adicionar à fila: "))

for _ in range(numElementos):
    elemento = input("Digite o elemento para adicionar à fila: ")
    fila.enqueue(elemento)

print("Elemento da frente da fila:", fila.front())

removerElemento = input("Digite o elemento que deseja remover da fila: ")
if removerElemento in fila.queue:
    fila.queue.remove(removerElemento)
    print("Elemento removido da fila:", removerElemento)
else:
    print("Elemento não encontrado na fila.")

print("Elemento da frente da fila após remover o elemento é:", fila.front())
