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
    contas = []
    endereco = {"logradouro": '',
                "bairro": '',
                "cidade": '',
                "estado": '',
                }
    usuario = {"CPF": '',
               "nome": '',
               "endereco": endereco,
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
                criar_conta(usuarios, usuario)
            case "d":
                depositar()
            case "e":
                extrato()
            case "u":
                criar_usuario(usuarios, usuario)
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


def criar_usuario(usuarios: list, usuario: dict):
    print_opcao("criar usuario")
    
    print(usuarios)
    novo_usuario = preencher_dados(usuario, usuarios)
    if novo_usuario:
        print(novo_usuario)
        usuarios.append(novo_usuario)

def print_opcao(texto:str) -> None:
    print()
    print("   ", "=" * 40)
    print("\t\t", texto)
    print("   ", "=" * 40)
    print()


def preencher_dados(campos: dict, contexto: list = []) -> dict:
    novo_usuario = {}
    for campo in campos:
        if isinstance(campos[campo], str):
            mensagem = f'\t{campo}: '
            novo_usuario[campo] = input(mensagem)
            if valida_campo(campo, novo_usuario[campo], contexto) == False:
                return

        elif isinstance(campos[campo], dict):
            print_opcao("endereco: ")
            novo_usuario[campo] = preencher_dados(campos[campo])

    return novo_usuario


def valida_campo(campo: str, valor: str, contexto: list = []) -> bool:
    match campo:
        case 'CPF':
            if not valor.isdigit():
                print("CPF Inválido, favor digitar apenas numeros")
                return False
            elif lista_cpfs(valor, contexto):
                print("CPF já cadastrado")
                print()

                ### To do imprimir usuario)
                return False
    return True


def lista_cpfs(cpf:str, usuarios: list) -> dict:
    usuario = [usuario for usuario in usuarios if usuario['CPF'] == cpf]
    return usuario[0] if usuario else None



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
