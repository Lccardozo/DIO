contas = {
    1000: {"Saldo": 2000.00, "Limite": 200.00, "Numero_Saques": 0, "Limite_Saques": 3, "Agencia": "0001"},
    1001: {"Saldo": 3000.00, "Limite": 500.00, "Numero_Saques": 0, "Limite_Saques": 4, "Agencia": "0001"},
    1002: {"Saldo": 1000.00, "Limite": 100.00, "Numero_Saques": 0, "Limite_Saques": 2, "Agencia": "0001"},
}

def menu():
    menu = """ Selecione
    [c] Criar conta
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """
    print(menu)

def criar_conta():
    print("Bem Vindo a criação de contas")
    print("Digite as informações da conta")
    Saldo = float(input("O Saldo da conta: "))
    Limite = float(input("Limite da conta: "))
    LimiteSaque = int(input("Limite de saques: "))
    Agencia = "0001"
    Conta = max(contas.keys()) + 1 if contas else 1000
    contas[Conta] = {"Saldo": Saldo, "Limite": Limite, "Limite_Saques": LimiteSaque, "Numero_Saques": 0, "Agencia": Agencia}
    print(f"Conta {Conta} criada com sucesso!")

def login():
    print("Digite o numero da sua conta")
    global numero_conta
    numero_conta = int(input("Conta: "))
    
    if numero_conta in contas.keys():
        return numero_conta
    else:
        print("Conta não encontrada.")
        return None

def deposito(Saldo, Valor_Deposito):
    Saldo += Valor_Deposito
    print(f'Seu novo saldo é {Saldo:.2f}')
    return Saldo

def saque(Saldo, Limite, Valor_Saque, NumeroSaques, LimiteSaques):
    valor_saque_total = Saldo + Limite   

    print("Verificando Saque")
    if Valor_Saque > valor_saque_total or NumeroSaques == LimiteSaques:
           print("Impossivel sacar")   
           return Saldo, NumeroSaques
           
    elif Valor_Saque < valor_saque_total and NumeroSaques < LimiteSaques:
            Saldo = Saldo - Valor_Saque               
            print(f'Seu saldo atual é {Saldo:.2f}') 
            NumeroSaques = NumeroSaques + 1
            return Saldo, NumeroSaques    

def extrato(Saldo, Limite, NumeroSaques, LimiteSaques):
    print(f'Seu saldo é {Saldo:.2f} e seu limite é {Limite:.2f}\n Seu Numero de Saques é {NumeroSaques} de {LimiteSaques}')

def main():
    print("Bem-Vindo")
    login()
    if numero_conta is None:
        return

    Saldo = contas[numero_conta]["Saldo"]
    Limite = contas[numero_conta]["Limite"]
    NumeroSaques = contas[numero_conta]["Numero_Saques"]
    LimiteSaques = contas[numero_conta]["Limite_Saques"]

    while True:
        menu()
        opcao = input("Selecione uma opção: ")
        if opcao == "d":
            Valor_Deposito = float(input("Digite o valor do deposito: "))
            Saldo = deposito(Saldo, Valor_Deposito)
        elif opcao == "s":
            print("Bem-Vindo ao sistema de Saque")
            print("Digite o valor a ser sacado")   
            Valor_Saque = float(input("Valor: "))
            Saldo, NumeroSaques = saque(Saldo, Limite, Valor_Saque, NumeroSaques, LimiteSaques)
        elif opcao == "e":
            extrato(Saldo, Limite, NumeroSaques, LimiteSaques)
        elif opcao == "c":
            criar_conta()
        elif opcao == "q":
            print(contas)
            break
        else:
            print("Opção inválida")

main()
