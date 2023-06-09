class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)


def verificaPalindromo(frase):
    fila = Queue()
    for caractere in frase:
        if caractere.isalnum():
            fila.enqueue(caractere.lower())

    while not fila.is_empty():
        if fila.dequeue() != fila.queue.pop():
            return False

    return True

frase = input("Digite uma frase: ")

frase = ''.join(e for e in frase if e.isalnum())

if verificaPalindromo(frase):
    print("A frase é um palíndromo.")
else:
    print("A frase não é um palíndromo.")
