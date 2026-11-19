from dataclasses import dataclass
@dataclass
class RegistroCliente:
    NomeCliente: str = ''
    TelefoneCliente: str = ''

def registrarCliente():
    registro = RegistroCliente()
    while True: 
        nome = input('Nome do Cliente: ').strip()
        if nome:
            registro.NomeCliente = nome
            break
        else:
            print('O nome não pode ficar vazio!')

    while True:
        numero = input('Telefone do Cliente((XX) X XXXX-XXXX): ').strip().replace(' ', '').replace('-', '').replace('(', '').replace(')', '')
        if numero.isdigit() and len(numero) == 11:
            registro.TelefoneCliente = numero
            break 
        else:
            print('Telefone inválido! Utilize apenas números e formato brasileira (XX) X XXXX-XXXX.')
    return registro
    
def listarClientes(lista):
    if len(lista) == 0:
        print('Sem clientes cadastrados!')
    else:
        for i in range(len(lista)):
            Telefone = lista[i].TelefoneCliente 
            ddd = Telefone[:2]
            parte1 = Telefone[2:7]
            parte2 = Telefone[7:] 
            print(f'Cliente {i}. Nome: {lista[i].NomeCliente}')
            print(f'Telefone: ({ddd}) {parte1}-{parte2}')
        
def contarClientes(lista):
    print(len(lista))

def carregarClientes():
    clientes = []
    arquivo = open('clientes.txt', 'a')
    arquivo.close()

    arquivo = open('clientes.txt', 'r')

    for linha in arquivo:
        if linha.strip():
            dados = linha.strip().split(';')
            registro = RegistroCliente(dados[0],dados[1])
            clientes.append(registro)
    arquivo.close()
    return clientes

def salvarClientes(lista):
    arquivo = open('clientes.txt', 'w')

    for cliente in lista:
        arquivo.write(f'{cliente.NomeCliente};{cliente.TelefoneCliente}\n')
    arquivo.close()


def atualizarClientes(lista):

    if len(lista) == 0:
        print('Sem clientes cadastrados.')
        return

    listarClientes(lista)

    indice = int(input('Digite o número do que cliente deseja atualizar: '))

    if 0 <= indice < len(lista):
        clienteSelecionado = lista[indice]
    else:
        print('Opção inválida.')
        return

    while True:
        print('Digite oque deseja alterar.')
        print('1- Nome.\n2- Telefone.')
        opcao = input('Digite a opção: ')
        if opcao == '1':
            clienteSelecionado.NomeCliente = input('Digite o novo nome: ')

        elif opcao == '2':
            clienteSelecionado.TelefoneCliente = input('Digite o novo telefone: ')

        else:
            print('opção inválida.')
            break