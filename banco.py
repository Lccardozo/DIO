menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

Saldo = 2000.00
Limite = 200.00
Extrato = Saldo
Numero_Saques = 0
Limite_Saques = 3




while True:
    print("BEM-VINDO AO BANCO")
    opcao = input(menu)

    if opcao == "d":
        print("Bem-vindo ao deposito")
        Deposito = float(input("Valor a ser depositado: "))
        Saldo =+ Deposito

    elif opcao == "s":
        print("Faça seu saque: ")
        Saque = float(input("Valor a ser sacado: "))
        if Saque >= Saldo + Limite or Limite_Saques == Numero_Saques:
            print("Não foi possivel realizar o saque" )
        
        elif Saque <= Saldo + Limite and Numero_Saques <= Limite_Saques:    
            Saldo = Saldo-Saque
            Numero_Saques = Numero_Saques+1
            print("Saque realizado com sucesso!")

        

    elif opcao == "e":
        print(f"R${Saldo:.2f}")
        print(f"R${Limite:.2f}")
        print(f"{Numero_Saques} de {Limite_Saques}")

        
            


    elif opcao == "q":
        break

    else:
        print("Opção invalida")











