"""
Contem os desafios feitos
    1: Criando um Sistema Bancario
    2: Otimizando o Sistema Bacario com Funções em python
    3: POO
        1 - Modelando o Sistema Bancario em POO com Python
        2 - Decoradores, Iteratores e Geradores com Python
        3 - Lidando com Data, Hora e Fuso Horário no Python

"""

from abc import ABC, abstractmethod, abstractproperty
from textwrap import dedent
from time import localtime, strftime, time



# FunÃ§Ã£o mai
def main():
    desafio = ''
    while desafio != 'q':
        desafio = input(exibe_menu("escolhe_desafio"))
        match desafio:
            case '1':
                print()
                print("=" * 40 )
                print("\tEntrando no desafio 1!")
                print("=" * 40 )
                print()
                desafio_1()

            case '2':
                print()
                print("=" * 40 )
                print("\tEntrando no desafio 2!")
                print("=" * 40 )
                print()
                desafio_2()

            case '3':
                print()
                print("=" * 40 )
                print("\tEntrando no desafio 3!")
                print("=" * 40 )
                print()
                desafio_3()
        
            case 'q':
                print()
                print("=" * 40 )
                print("\t\tSaindo...")
                print("=" * 40 )
                print()
            
            case _:
                print("=" * 40 )
                print("\t\tOpÃ§Ã£o Invalida...")
                print("=" * 40 )


def exibe_menu(menu: str) -> str:
    escolhe_desafio = """

    [1]\tDesafio 1 - Python Basico
    [2]\tDesafio 2 - Estrutura de Dados
    [3]\tDesafio 3 - POO
    ======================================
    [q]\tSair

    Digite a Opca£o Desejada: """

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
    
    Digite a opca£o desejada: """


    menus = {}
    menus["escolhe_desafio"] = escolhe_desafio
    menus["desafio_2"] = desafio_2


    return menus[menu]


def desafio_2():
    """ ImplementaÃ§Ã£o do segundo desafio de python."""

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
    
    conta = {"conta": "0",
             "agencia": "0001",
             'cpf': '',
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
                sacar(contas=contas)
            case "c":
                criar_conta(usuarios, contas, conta)
            case "d":
                depositar(contas)
            case "e":
                extrato(contas, usuarios=usuarios)
            case "u":
                criar_usuario(usuarios, usuario)
            case "l":
                lista_contas(contas)
            case "q":
                print_opcao("Saindo")
                return 
            case _:
                print_opcao("OpÃ§Ã£o invalida!")


def busca_conta(contas: list) -> dict:
    numero_conta = input("\tNumero da Conta: ")
    conta = [conta for conta in contas if conta['conta'] == numero_conta]
    
    return conta[0] if conta else None



def sacar(*, contas: list) -> None:
    print_opcao("sacar")
    conta = busca_conta(contas)
    if not conta:
        print("\tConta nÃ£o localizada")
        return

    if not conta['saques']:
        print("\tLimite de saque atingido!!!")
        return

    valor = float(input('\tValor: '))
    if valor > 500:
        print("\tValor maior que o limite.")
        return
    elif valor > conta['saldo']:
        print("\tSaldo insulficiente!!!")
        return
    
    conta['saques'] -= 1
    conta['saldo'] -= valor
    conta['extrato'].append(["Saque   ", valor])


    imprime_contas(conta['cpf'], contas)

    


def depositar(contas: list, /) -> None:
    print_opcao("depositar")
    conta = busca_conta(contas)
    if not conta:
        print("\tConta nÃ£o localizada")
        return
    
    valor = float(input('\tValor: '))
    conta['saldo'] += valor
    conta['extrato'].append(['deposito', valor])
    imprime_contas(conta['cpf'], contas)


def extrato(contas: list, /, *, usuarios: list) -> None:
    print_opcao("extrato")
    conta = busca_conta(contas)
    if not conta:
        print("\tConta nÃ£o localizada")
        return
    
    cpf = conta['cpf']
    usuario = lista_cpfs(cpf, usuarios)

    print("\t==================================")
    print(f"\t=  Cliente: {usuario['nome']} - CPF: {usuario['CPF']} \t=")
    print("\t==================================")
    print("=\tOperaÃ§Ã£o\t-----\tValor\t=")
    for operacao, valor in conta['extrato']:
        print(f"\t{operacao}\t-----\tR$ {valor:.2f}")
    print("\t==================================")
    print(f"\tSaldo\t-----\tR$ {conta['saldo']:.2f}")






def lista_contas(contas: list):
    print_opcao("listar contas")
    cpf = input("\tCPF: ")
    if valida_campo("CPF", cpf) == False:
        return

    contas_cpf = [conta for conta in contas if conta['cpf'] == cpf]
    if not contas_cpf:
        print("Conta nÃ£o encontrada para esse CPF")
        return
    
    imprime_contas(cpf, contas_cpf)

    
    
    
def imprime_contas(cpf: str, contas: list) -> None:
    print_opcao(f"CONTA - CPF {cpf}")
    for  conta in contas:
        imprime_campos(conta)
        print('\n\n   ============================\n')


def imprime_usuario(cpf: str, usuarios: list) -> None:
    usuario = lista_cpfs(cpf, usuarios)
    if not usuario:
        print("UsuÃ¡rio não encontrado!")
        return
    print_opcao("Usuario")

    imprime_campos(usuario)


def imprime_campos(dicionario: dict, tab: int=1):
    print()
    for campo, valor in dicionario.items():
        print("\t" * tab, campo, ": ", sep='', end='')
        if isinstance(valor, dict):
            imprime_campos(valor, tab + 1)
        else:
            print(valor)




def imprime_conta(numero_conta: str, contas: list) -> None:
    print(contas[int(numero_conta) - 1])


def criar_conta(usuarios: list, contas: list, conta: dict) -> None:
    print_opcao("criar conta")

    cpf = input("Digite o CPF: ")
    if valida_campo('cpf', cpf) == False:
        return

    if not lista_cpfs(cpf, usuarios):
        print("Usuario nÃ£o cadastrado!!!")
        print("Favor cadastrar o usuario primeiro!!!")
        return

    nova_conta = dict(conta)
    nova_conta['cpf'] = cpf
    nova_conta['conta'] = str(len(contas) + 1)

    contas.append(nova_conta)
    
    imprime_conta(nova_conta['conta'], contas)


def criar_usuario(usuarios: list, usuario: dict):
    print_opcao("criar usuario")
    
    print(usuarios)
    novo_usuario = preencher_dados(usuario, usuarios)
    if novo_usuario:
        print(novo_usuario)
        usuarios.append(novo_usuario)
        
        imprime_usuario(novo_usuario['CPF'], usuarios)

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
                print("CPF InvÃ¡lido, favor digitar apenas numeros")
                return False
            elif lista_cpfs(valor, contexto):
                print("CPF jÃ¡ cadastrado")
                print()

                ### To do imprimir usuario)
                return False
    return True


def lista_cpfs(cpf:str, usuarios: list) -> dict:
    usuario = [usuario for usuario in usuarios if usuario['CPF'] == cpf]
    return usuario[0] if usuario else None



# FunÃ§Ã£o do desafio 1
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
        opcao = input("Digite a opÃ§Ã£o desejada: ")

        if opcao == 'd':
            print("===== Depositar =====\n")
            valor = float(input("Digite o valor do depÃ³sito: "))
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
                print("Limite de saques diÃ¡rios atingido!")
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
                print("Valor de saque excede limite mÃ¡ximo de ", end='')
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
                    print(f"DepÃ³sito de R$ {deposito[d]:.2f}")
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
            print("OpÃ§Ã£o invÃ¡lida!")


class Transacao(ABC):

    def decorador_de_log(funcao):
        def registro(*args, **kwargs):
            funcao(*args, **kwargs)
            self, conta = args
            data_hora = strftime("%x %X")
            status = "Erro" if self.status else "Ok"
            operacao = self.__class__.__name__
            cliente = conta.cliente.nome
            c_c = conta.numero_conta
            saldo = conta.saldo
            
            log = (f"{data_hora} - {status} - {operacao} -"
                   f"Cliente: {cliente} - C/C: {c_c} - saldo: R$ {saldo:.2f}"
                   f" - {self.mensagem}")

            print(log)

        return registro

    @abstractmethod
    def registrar(self, conta):
        pass


    @abstractproperty
    def valor(self):
        pass


class Deposito(Transacao):
    def __init__(self, valor: str) -> None:
        self._valor = valor

    
    @property
    def valor(self):
        return self._valor


    @Transacao.decorador_de_log
    def registrar(self, conta):
        self.status = conta.depositar(self.valor)

        match self.status:
            case 0:
                self.mensagem = "Deposito efetuado com sucesso"
            case _:
                self.mensagem = "Valor menor que 0"
        
        conta.historico.adicionar_transacao(self)


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    @Transacao.decorador_de_log
    def registrar(self, conta):
        self.status = conta.sacar(self.valor)
        match self.status:
            case 0:
                self.mensagem = "Saque realizado com sucesso"
            case 1:
                self.mensagem = "Valor incorreto <0"
            case 2:
                self.mensagem = "Saldo insuficiente"
            case 3:
                self.mensagem = "Numero de saques diarios excedido"
            case 4:
                self.mensagem = "Valor do saque excedido"
        
        conta.historico.adicionar_transacao(self)

class Historico:
    def __init__(self):
        self._transacoes = []

    
    @property
    def transacoes(self):
        return self._transacoes


    def adicionar_transacao(self, transacao):
        self._transacoes.append({"tipo": transacao.__class__.__name__,
                                 "valor": transacao.valor,
                                 "data": time(),
                                 "status": transacao.status,
                                 "mensagem": transacao.mensagem
                                 })

    def relatorio_transacoes(self, tipo = "ALL"):
        for transacao in self._transacoes:
            if tipo == "ALL" or tipo.lower() == transacao["tipo"].lower():
                yield transacao



class Cliente:
    def __init__(self, endereco):
        self._edereco = endereco
        self._contas = []
        self.__limite_transacoes = 10

    
    @property
    def endereco(self):
        return self._endereco

    
    @property
    def contas(self):
        return self._contas

    def realiza_transacao(self, conta: 'Conta', transacao: Transacao) -> None:
        
        qtd_transacoes = sum(1 for transacao in conta.historico.transacoes if
                                transacao["status"] == 0 and
            strftime("%x") == strftime("%x", localtime(transacao["data"])))
        
        if qtd_transacoes >= self.__limite_transacoes:
            transacao.status = 1
            transacao.mensagem = "Limite de transacoes por dia excedido"
            conta.historico.adicionar_transacao(transacao) 
        else:
            transacao.registrar(conta)

        

    def adiciona_conta(self, numero_conta):
        conta = ContaCorrente(numero_conta, self)
        self._contas.append(conta)
        return conta


class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

    @property
    def cpf(self):
        return self._cpf

    @property
    def nome(self):
        return self._nome

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @classmethod
    def busca_cliente(cls, clientes: list, cpf: str = None) -> Cliente:
        cliente = [cliente for cliente in clientes if cliente.cpf == cpf]
        return cliente[0] if cliente else None

    def __str__(self):
        contas = [conta.numero_conta for conta in self.contas]
        return f"""\
                nome:\t{self.nome}
                contas:\t{contas}"""


class Conta:
    def __init__(self, numero_conta: int, cliente: Cliente):
        self._numero_conta = numero_conta
        self._cliente = cliente
        self._agencia = "0001"
        self._historico = Historico()
        self._saldo = 0

    
    @property
    def numero_conta(self):
        return self._numero_conta


    @property
    def cliente(self):
        return self._cliente

    
    @property
    def agencia(self):
        return self._agencia


    @property
    def saldo(self):
        return self._saldo

    
    @property
    def historico(self):
        return self._historico


    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)


    def depositar(self, valor):
        if valor >= 0:
            self._saldo += valor
            return 0
        else:
            return 1


    def sacar(self, valor):
        if valor <= 0:
            # valor invalido
            return 1

        elif valor > self.saldo:
            # excedeu o saldo
            return 2

        else:
            # sucesso na operacao
            self._saldo -= valor
            return 0

    @property
    def extrato(self):
        print("=== Extrato ===")
        print(f"Cliente: {self.cliente.nome}")
        print(f"CPF: {self.cliente.cpf}")
        print(f"Conta: {self.numero_conta}")
        print("===============")
        if not self.historico.transacoes:
            print("Conta sem movimentação")
            return
        transacoes = [transacao for transacao in self.historico.transacoes 
                      if transacao["status"] == 0]
        for transacao in transacoes:
            d = localtime(transacao['data'])
            data = strftime("%x %X", d)
            print(f"{data} - {transacao['tipo']} - R$ {transacao['valor']:.2f}")
        print()
        print("===============")
        print(f"Saldo:\t\t R$ {self.saldo:.2f}")
        print("===============")


class ContaCorrente(Conta):
    def __init__(self, numero_conta: str, cliente: Cliente) -> None:
        super().__init__(numero_conta, cliente)
        self.__valor = 500
        self.__quantidade_max = 3 



    def sacar(self, valor):

        quantidade_saques = sum(1 for transacao in self.historico.transacoes if
                                transacao["tipo"] == "Saque" and
                                transacao["status"] == 0)

        if quantidade_saques >= self.__quantidade_max:
            return 3

        elif valor > self.__valor:
            return 4

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
                Agência:\t{self.agencia}
                C/C:\t\t{self.numero_conta}
                Titular:\t{self.cliente.nome}
                """


class ContaIterator:
    def __init__(self, contas: list[Conta]) -> None:
        self._contas = contas
        self._index = 0
        self._end = len(contas)


    def __iter__(self):
        return self

    def __next__(self):
        if self._index == self._end:
            raise StopIteration
        conta = self._contas[self._index]
        self._index += 1
        return {"numero": conta.numero_conta,
                "cliente": conta.cliente.nome,
                "saldo": conta.saldo,
                "cpf": conta.cliente.cpf}


def desafio_3():
    clientes = []
    contas = []

    # --- Testes
    test_cria_clientes(clientes)
    contas.append(test_adiciona_conta(clientes[0], len(contas) + 1))
    contas.append(test_adiciona_conta(clientes[1], len(contas) + 1))
    contas.append(test_adiciona_conta(clientes[0], len(contas) + 1))
    contas.append(test_adiciona_conta(clientes[0], len(contas) + 1))


    [print(cliente) for cliente in clientes]
    
    print(clientes[0].contas[0].cliente.nome)
    # deposito

    clientes[0].realiza_transacao(contas[0], Deposito(1000))
    clientes[0].realiza_transacao(contas[0], Deposito(-650))

    clientes[0].realiza_transacao(contas[0], Saque(100))
    clientes[0].realiza_transacao(contas[0], Saque(750))
    clientes[0].realiza_transacao(contas[0], Saque(490))
    clientes[0].realiza_transacao(contas[0], Saque(-50))
    clientes[0].realiza_transacao(contas[0], Saque(450))
    clientes[0].realiza_transacao(contas[0], Saque(50))
    clientes[0].realiza_transacao(contas[0], Saque(50))
    clientes[0].realiza_transacao(contas[0], Deposito(1000))
    clientes[0].realiza_transacao(contas[0], Deposito(1000))
    clientes[0].realiza_transacao(contas[0], Deposito(1000))
    clientes[0].realiza_transacao(contas[0], Deposito(1000))
    clientes[0].realiza_transacao(contas[0], Deposito(1000))
    clientes[0].realiza_transacao(contas[0], Deposito(1000))
    clientes[0].realiza_transacao(contas[0], Deposito(1000))
    clientes[0].realiza_transacao(contas[0], Deposito(1000))
    clientes[0].realiza_transacao(contas[0], Deposito(1000))
    clientes[0].realiza_transacao(contas[0], Deposito(1000))
    clientes[0].realiza_transacao(contas[0], Deposito(1000))
    clientes[0].realiza_transacao(contas[0], Deposito(1000))
    clientes[0].realiza_transacao(contas[0], Deposito(1000))
    clientes[0].realiza_transacao(contas[0], Deposito(1000))
    clientes[0].realiza_transacao(contas[0], Deposito(1000))
    clientes[0].realiza_transacao(contas[0], Deposito(1000))
    clientes[0].realiza_transacao(contas[0], Deposito(1000))
    clientes[0].realiza_transacao(contas[0], Deposito(1000))
    clientes[0].realiza_transacao(contas[0], Deposito(1000))
    clientes[0].realiza_transacao(contas[0], Deposito(1000))

    [print(historico) for historico in clientes[0].contas[0].historico.relatorio_transacoes("deposito")]

    clientes[0].contas[0].extrato

    for conta in ContaIterator(contas):
        info = (f"Conta: {conta['numero']} - Cliente: {conta['cliente']} - "
                f"CPF: {conta['cpf']} - saldo: {conta['saldo']}")
        print(info)


    # --- Fim do teste

    print("Desafio 3")
    while True:
        opcao = input(exibe_menu('desafio_2'))

        match opcao:
            case "q":
                print_opcao("Saindo...")
                break
            case "c":
                """ Cadastrar conta"""
                print_opcao('Criar conta')
                cpf = input("\tCPF do Cliente: ")
                cliente = Cliente.busca_cliente(clientes, cpf)

                if cliente:
                    contas.append(cliente.adiciona_conta(len(contas)))

            case "u":
                """  Criar novo cliente. """
                print_opcao("Cadastrar cliente")
                cpf = input("\tCPF: ")
                nome = input("\tnome: ")
                data_nascimento = input("\tdata nascimento: ")
                endereco = input("\tEndereco: ")
                
                clientes.append(PessoaFisica(endereco, 
                                             cpf, 
                                             nome, 
                                             data_nascimento))

            case _:
                print_opcao("Opcao invalida")


def test_cria_clientes(clientes):

    clientes.append(PessoaFisica(
                                 "123456789",
                                 "Joao",
                                 "01/01/2000",
                                 "Rua imaginario"))
    
    clientes.append(PessoaFisica(
                                 "987654321",
                                 "Abgail",
                                 "01/01/2010",
                                 "Rua imaginario1"))

def test_adiciona_conta(cliente, numero_conta):
     return cliente.adiciona_conta(numero_conta)



#  Ponto de entrada do programa
if __name__ == "__main__":
    
    main()
