# banco.py - Sistema Bancário em POO

# =======================
# Classes do sistema
# =======================

class Cliente:
    def __init__(self, nome):
        self.nome = nome

class Conta:
    def __init__(self, numero, titular: Cliente):
        self.numero = numero
        self.titular = titular
        self.saldo = 0.0
        self.historico = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.append(f"Depósito: R${valor:.2f}")
            print(f"Depósito de R${valor:.2f} realizado na conta {self.numero}.")
        else:
            print("Valor inválido!")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido!")
        elif valor <= self.saldo:
            self.saldo -= valor
            self.historico.append(f"Saque: R${valor:.2f}")
            print(f"Saque de R${valor:.2f} realizado da conta {self.numero}.")
        else:
            print("Saldo insuficiente!")

    def extrato(self):
        print(f"\nExtrato da conta {self.numero} - {self.titular.nome}:")
        for operacao in self.historico:
            print(operacao)
        print(f"Saldo atual: R${self.saldo:.2f}\n")

# =======================
# Função do menu
# =======================

def menu():
    contas = []  # lista para armazenar objetos Conta

    while True:
        print("\n=== Sistema Bancário ===")
        print("1 - Criar cliente e conta")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Ver extrato")
        print("5 - Listar clientes")
        print("6 - Listar contas")
        print("7 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            numero = input("Número da conta: ")
            titular_nome = input("Nome do titular: ")
            cliente = Cliente(titular_nome)
            conta = Conta(numero, cliente)
            contas.append(conta)
            print(f"Conta {numero} criada para {titular_nome}!")

        elif opcao == "2":
            numero = input("Número da conta: ")
            conta = next((c for c in contas if c.numero == numero), None)
            if conta:
                try:
                    valor = float(input("Valor do depósito: "))
                    conta.depositar(valor)
                except ValueError:
                    print("Digite um valor numérico válido!")
            else:
                print("Conta não encontrada!")

        elif opcao == "3":
            numero = input("Número da conta: ")
            conta = next((c for c in contas if c.numero == numero), None)
            if conta:
                try:
                    valor = float(input("Valor do saque: "))
                    conta.sacar(valor)
                except ValueError:
                    print("Digite um valor numérico válido!")
            else:
                print("Conta não encontrada!")

        elif opcao == "4":
            numero = input("Número da conta: ")
            conta = next((c for c in contas if c.numero == numero), None)
            if conta:
                conta.extrato()
            else:
                print("Conta não encontrada!")

        elif opcao == "5":
            if contas:
                print("\nClientes cadastrados:")
                for i, conta in enumerate(contas, 1):
                    print(f"{i} - {conta.titular.nome}")
            else:
                print("Nenhum cliente cadastrado.")

        elif opcao == "6":
            if contas:
                print("\nContas cadastradas:")
                for conta in contas:
                    print(f"Conta {conta.numero} - Titular: {conta.titular.nome} - Saldo: R${conta.saldo:.2f}")
            else:
                print("Nenhuma conta cadastrada.")

        elif opcao == "7":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

# =======================
# Executar o menu
# =======================
if __name__ == "__main__":
    menu()
