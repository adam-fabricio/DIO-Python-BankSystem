# __main__.py

# importações necessárias
import os
import platform



#  Função main
def main():
    desafio = ''
    while desafio != 'q':
        desafio = input(exibe_menu("escolhe_desafio"))
        if desafio == '1':
            print()
            print("=" * 40 )
            print("\tEntrando no desafio 1!")
            print("=" * 40 )
            print()
            desafio_1()

        elif desafio == '2':
            print()
            print("=" * 40 )
            print("\tEntrando no desafio 2!")
            print("=" * 40 )
            print()
            desafio_2()
        elif desafio == 'q':
            print()
            print("=" * 40 )
            print("\t\tSaindo...")
            print("=" * 40 )
            print()
        
        else:
            print("=" * 40 )
            print("\t\tOpção Invalida...")
            print("=" * 40 )


def exibe_menu(menu: str) -> str:
    escolhe_desafio = """

    [1]\tDesafio 1
    [2]\tDesafio 2
    ========================
    [q]\tSair

    Digite a Opção Desejada: """

    desafio_2 = """
    ================================
        Bom vindo ao AdamBank!!!
    ================================

    [c]\tCadastrar nova Conta
    [d]\tDepositar
    [e]\tExtrato
    [s]\tSacar
    [u]\tCadastrar novo Usuario
    [l]\tListar contas
    [q]\tSair
    ================================
    
    Digite a opção desejada: """


    menus = {}
    menus["escolhe_desafio"] = escolhe_desafio
    menus["desafio_2"] = desafio_2


    return menus[menu]


def desafio_2():
    """ Implementação do segundo desafio de python."""

    usuarios = []
    endereco = {"logradouro": '',
                "bairro": '',
                "cidade": '',
                "estado": '',
                }
    usuario = {"nome": '',
               "cpf": '',
               "endereco": endereco,
               "contas": [],
               }
    conta_corrente = []
    conta = {"conta": "0",
             "agencia": "0001",
             "saldo": 0,
             "saques": 3,
             "extrato": []
             }
    operacoes = {"operacao": '',
                 "valor": ''
                 }


    
    print("Bem vindo ao desafio 2")
    opcao = ''

    while opcao != 'q':
        opcao = input(exibe_menu("desafio_2"))

        match opcao:
            case "s":
                sacar()
            case "c":
                criar_conta()
            case "d":
                depositar()
            case "e":
                extrato()
            case "u":
                criar_usuario()
            case "l":
                listar_contas()
            case "q":
                print_opcao("Saindo")
                return 
            case _:
                print_opcao("Opção invalida!")


def sacar():
    print_opcao("sacar")


def depositar():
    print_opcao("depositar")


def extrato():
    print_opcao("extrato")


def listar_contas():
    print_opcao("listar contas")


def criar_conta():
    print_opcao("criar conta")


def criar_usuario():
    print_opcao("criar usuario")


def print_opcao(texto:str) -> None:
    print()
    print("   ", "=" * 40)
    print("\t\t", texto)
    print("   ", "=" * 40)
    print()




# Função do desafio 1
def desafio_1():
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
