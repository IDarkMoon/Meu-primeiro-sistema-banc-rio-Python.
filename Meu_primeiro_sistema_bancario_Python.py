menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
       valor = float(input("Digite o valor de depósito:"))
       if valor > 0:
           saldo += valor
           extrato += f"Depósito: R$ {valor:.2f}\n"

       else:
           print("Inválido. Favor digitar valor dentro do limite.")

    elif opcao == "2":
        valor = float(input("Digite o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Inválido. Seu saldo não é suficiente.")

        elif excedeu_limite:
            print("Inválido. Valor digitado excede o limite permitido.")

        elif excedeu_saques:
            print("Inválido. Número de saques maior que o permitido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else: ("Inválido. Digite um valor válido.")

 
    

    elif opcao == "3":
        print("\n==========Extrato==========")
        print("Sem movimentações recentes." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=============================")

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")



#KeiteMascena

