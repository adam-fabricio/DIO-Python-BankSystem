# __main__.py

# importações necessárias
import os
import platform


# Função principal
def main():
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """
    opcao = ''
    saldo = 0
    deposito = []
    saque = []
    extrato = []
    LIMITE_SAQUE = 3
    LIMITE_VALOR_SAQUE = 500

    while opcao != 'q':
        print("\n" * 2)
        print(f"Saldo: R$ {saldo:.2f}")

        print(menu)
        opcao = input("Digite a opção desejada: ")

        if opcao == 'd':
            print("===== Depositar =====\n")
            valor = float(input("Digite o valor do depósito: "))
            if valor < 0:
                print("Valor invalido!!!")
                continue
            saldo += valor
            deposito.append(valor)
            extrato.append(1)
            print(f"Depósito de R$ {valor:.2f}!")

        elif opcao == 's':
            print("===== Sacar =====")
            print()
            if len(saque) >= LIMITE_SAQUE:
                print("Limite de saques diários atingido!")
                print()
                continue

            valor = float(input("Digite o valor do saque: "))
            if valor < 0:
                print("Valor invalido!!!")
                continue

            elif valor > saldo:
                print(f"Saldo atual de R$ {saldo:.2f}!")
                print("Saldo insuficiente!")
                continue

            elif valor > LIMITE_VALOR_SAQUE:
                print("Valor de saque excede limite máximo de ", end='')
                print(f"R$ {LIMITE_VALOR_SAQUE:.2f}")

                continue

            else:
                saldo -= valor
                saque.append(valor)
                extrato.append(0)

        elif opcao == 'e':
            print("===== Extrato =====")
            s = 0
            d = 0
            for operacao in extrato:
                if operacao == 1:
                    print(f"Depósito de R$ {deposito[d]:.2f}")
                    d += 1
                elif operacao == 0:
                    print(f"Saque de R$ {saque[s]:.2f}")
                    s += 1
            print()
            print("=" * 20)
            print(f"Saldo: R$ {saldo:.2f}")
            print("=" * 20)

        elif opcao == 'q':
            print("Saindo...")

        else:
            print("Opção inválida!")


#  Ponto de entrada do programa
if __name__ == "__main__":
    main()
