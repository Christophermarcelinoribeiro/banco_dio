from datetime import datetime


def menu():
    return f"=======================================\nSacar[1] \nDepositar[2] \nExtrato[3] \nSair[4]\n======================================="


def extrato(lista_saque, lista_deposito, saldo):
    # SAQUE
    data = datetime.now()
    # For para percorre toda a lista_saque e printar seus valores junto com a data
    for x in lista_saque:

        print(f'Saque de.....R${x:.2f}.....data: {data.strftime("%d/%m/%Y %H:%M")}')
    # DEPOSITO
    for y in lista_deposito:
        # For para percorre toda a lista_deposito e printar seus valores junto com a data
        print(f'Deposito de.....R${y:.2f}.....data: {data.strftime("%d/%m/%Y %H:%M")}')

    print(f'Saldo de.....R${saldo:.2f}.....data: {data.strftime("%d/%m/%Y %H:%M")}')


saldo = 1000
limite_saque = 3
lista_saque = []
lista_deposito = []

while True:
    print(menu())
    try:
        escolha = int(input(f"Escolha uma opção: "))
    except ValueError:
        print(f"Erro: a entrada '{escolha}' não pode ser convertida para float.")
    if escolha == 1:
        # SAQUE
        try:
            saque = float(input(f"Digite o Valor do saque: "))
        except ValueError:
            print(f"Erro: a entrada '{saque}' não pode ser convertida para float.")
        if saque > 500:
            # Condição se o saque for maior que 500
            print(f"Valor maximo de saque: R$ 500,00!")
        elif saque > saldo:
            # Condição se o saque for maio que o saldo
            print(f"Saldo insuficiente")
        elif saque <= 0:
            # Condição se o saque for menor/igual a zero
            print(f"Solicitação do saque tem que ser maior que zero")
        elif limite_saque <= 0:
            # Condição que informa quando o limite diario foi excedido
            print(f"Limite de saque diario excedido!")
        else:
            saldo = saldo - saque
            limite_saque -= 1
            # Inseri a variavel saque na lista_saque
            lista_saque.append(saque)
            print("Saque efetuado com sucesso!")
    elif escolha == 2:
        # DEPOSITO
        try:

            deposito = float(input(f"Insira o valor de deposito: "))
        except ValueError:
            print(f"Erro: a entrada '{deposito}' não pode ser convertida para float.")
        if deposito <= 0:
            # condição se o deposito for menor que zero
            print(f"Somente valores acima de ZERO")
        else:
            saldo += deposito
            # Inseri a variavel deposito na lista_deposito
            lista_deposito.append(deposito)
            print("Deposito efeutado com sucesso!")
    elif escolha == 3:
        # Extrato
        extrato(lista_saque, lista_deposito, saldo)
    elif escolha == 4:
        print(f"Até Mais!")
        break
    else:
        print("Comando invalido!")
        print("===================================")
