# banco.py - Sistema Bancário

# Função para criar conta
def criar_conta(contas, numero, titular):
    if numero in contas:
        print("Conta já existe!")
    else:
        contas[numero] = {"titular": titular, "saldo": 0.0, "historico": []}
        print(f"Conta {numero} criada para {titular}.")

# Função para depósito
def depositar(contas, numero, valor):
    if numero in contas:
        contas[numero]["saldo"] += valor
        contas[numero]["historico"].append(f"Depósito: R${valor:.2f}")
        print(f"Depósito de R${valor:.2f} realizado na conta {numero}.")
    else:
        print("Conta não encontrada!")

# Função para saque
def sacar(contas, numero, valor):
    if numero in contas:
        if contas[numero]["saldo"] >= valor:
            contas[numero]["saldo"] -= valor
            contas[numero]["historico"].append(f"Saque: R${valor:.2f}")
            print(f"Saque de R${valor:.2f} realizado da conta {numero}.")
        else:
            print("Saldo insuficiente!")
    else:
        print("Conta não encontrada!")

# Função para extrato
def extrato(contas, numero):
    if numero in contas:
        print(f"\nExtrato da conta {numero} - {contas[numero]['titular']}:")
        for operacao in contas[numero]["historico"]:
            print(operacao)
        print(f"Saldo atual: R${contas[numero]['saldo']:.2f}\n")
    else:
        print("Conta não encontrada!")

# Função para menu principal
def menu():
    contas = {}  # dicionário para armazenar contas
    while True:
        print("=== Sistema Bancário ===")
        print("1 - Criar conta")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Extrato")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            numero = input("Número da conta: ")
            titular = input("Titular: ")
            criar_conta(contas, numero, titular)
        elif opcao == "2":
            numero = input("Número da conta: ")
            valor = float(input("Valor do depósito: "))
            depositar(contas, numero, valor)
        elif opcao == "3":
            numero = input("Número da conta: ")
            valor = float(input("Valor do saque: "))
            sacar(contas, numero, valor)
        elif opcao == "4":
            numero = input("Número da conta: ")
            extrato(contas, numero)
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

# Executa o menu quando o arquivo for rodado
if __name__ == "__main__":
    menu()