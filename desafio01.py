menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITA_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("informe o valor do depósito: "))

        if valor_deposito < 0:
            print("Valor inválido para depósito")
        else:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"

    elif opcao == "s":
        valor_saque = float(input("Informe o valor do saque: "))

        if numero_saques >= LIMITA_SAQUES:
            print("Número de saques diários atingido")
        
        elif valor_saque > limite:
            print(f"Seu limite de saque diário é de {limite}")

        elif (saldo - valor_saque) < 0:
            print("Você não tem saldo suficiente para realizar o saque")

        elif valor_saque < 0:
            print("Valor inválido")

        else:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            print(numero_saques)
            numero_saques += 1
            print(numero_saques)

    elif opcao == "e":
        print("\n################ EXTRATO ################")
        print("Não foram ralizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("#########################################")

    elif opcao == "q":
        print("Saindo...")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")