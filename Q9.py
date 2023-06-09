class Cliente:
    def __init__(self, nome, numeroConta, saldo):
        self.nome = nome
        self.numero_conta = numeroConta
        self.saldo = saldo
        self.proximo = None


class ListaClientes:
    def __init__(self):
        self.primeiro = None

    def is_empty(self):
        return self.primeiro is None

    def inserirCliente(self, nome, numeroConta, saldo):
        novoCliente = Cliente(nome, numeroConta, saldo)

        if self.is_empty():
            self.primeiro = novoCliente
        else:
            atual = self.primeiro
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novoCliente

        print("Cliente inserido com sucesso.")

    def removerCliente(self, numeroConta):
        if self.is_empty():
            print("A lista de clientes está vazia.")
            return

        if self.primeiro.numero_conta == numeroConta:
            self.primeiro = self.primeiro.proximo
            print("Cliente removido com sucesso.")
            return

        atual = self.primeiro
        prev = None
        while atual is not None:
            if atual.numero_conta == numeroConta:
                prev.proximo = atual.proximo
                print("Cliente removido com sucesso.")
                return
            prev = atual
            atual = atual.proximo

        print("Cliente não encontrado.")

    def procurarCliente(self, numeroConta):
        if self.is_empty():
            print("A lista de clientes está vazia")
            return

        atual = self.primeiro
        while atual is not None:
            if atual.numero_conta == numeroConta:
                print("Cliente encontrado:")
                print("Nome:", atual.nome)
                print("Número da Conta:", atual.numero_conta)
                print("Saldo:", atual.saldo)
                return
            atual = atual.proximo

        print("Cliente não encontrado.")

listaClientes = ListaClientes()

listaClientes.inserirCliente("John Doe", 123456, 1000)
listaClientes.inserirCliente("Jane Smith", 789012, 5000)
listaClientes.inserirCliente("David Johnson", 345678, 2000)

listaClientes.procurarCliente(789012)

listaClientes.removerCliente(789012)
listaClientes.procurarCliente(789012)
