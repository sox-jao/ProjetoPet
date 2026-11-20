from dataclasses import dataclass

def separador():
    print(f'\n{50*'-'}\n')

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
        numero = input('Telefone do Cliente: ').strip().replace(' ', '').replace('-', '').replace('(', '').replace(')', '')
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
            print(f'Cliente {i+1}.\n Nome: {lista[i].NomeCliente}')
            print(f' Telefone: ({ddd}) {parte1}-{parte2}\n')
        
def contarClientes(lista):
    print(len(lista), 'Clientes cadastrados.')

def carregarClientes():
    clientes = []
    arquivo = open('Dados/clientes.txt', 'a')
    arquivo.close()

    arquivo = open('Dados/clientes.txt', 'r')

    for linha in arquivo:
        if linha.strip():
            dados = linha.strip().split(';')
            registro = RegistroCliente(dados[0],dados[1])
            clientes.append(registro)
    arquivo.close()
    return clientes

def salvarClientes(lista):
    arquivo = open('Dados/clientes.txt', 'w')

    for cliente in lista:
        arquivo.write(f'{cliente.NomeCliente};{cliente.TelefoneCliente}\n')
    arquivo.close()


def atualizarClientes(lista):

    if len(lista) == 0:
        print('Sem clientes cadastrados.')
        return

    listarClientes(lista)
    while True:

        indice = input('Digite o número do cliente deseja atualizar: ')
        if indice.isdigit():
            indice = int(indice) 
            indice -= 1
        
            if 0 <= indice < len(lista):
                clienteSelecionado = lista[indice]

                separador()

                while True:
                    print(f'Nome: {clienteSelecionado.NomeCliente}')
                    telefone = clienteSelecionado.TelefoneCliente
                    ddd = telefone[:2]
                    parte1 = telefone[2:7]
                    parte2 = telefone[7:]
                    print(f'Telefone: ({ddd}) {parte1}-{parte2}')
                    print('Digite oque deseja alterar.')
                    print('1- Nome.\n2- Telefone.\n0- Voltar')
                    opcao = input('Digite a opção: ')
                    if opcao == '1':
                        clienteSelecionado.NomeCliente = solicitarNome()
                        salvarClientes(lista)
                        print('Nome do cliente atualizado com sucesso.')
                        separador()
                        return

                    elif opcao == '2':
                        clienteSelecionado.TelefoneCliente = solicitarTelefone()
                        salvarClientes(lista)
                        print('Telefone do cliente atualizado com sucesso.')
                        separador()
                        return

                    elif opcao == '0':
                        print('Voltando.')
                        return
                
                    else:
                        print('Opção inválida. Digite uma opção válida.')
                

            else:
                print('Opção inválida. Digite um cliente válido.')

        elif indice.strip() == '':
            print('Este campo não pode ficar vazio.')
            print(50*'-')

        else:
            print('Digite apenas números.')
            print(50*'-')     

def solicitarNome():
    while True:
        nome = input('Nome do Cliente: ').strip()
        if nome:
            return nome
        print('O nome não pode ficar vazio.')

def solicitarTelefone():
    while True:
        telefone = input('Telefone do cliente: ').strip()
        telefone = telefone.replace(' ', '').replace('-', '').replace('(', '').replace(')', '')
        if telefone.isdigit and len(telefone) == 11:
            return telefone
        print('Telefone inválida! Utilize apenas números e formato brasileira (XX) X XXXX-XXXX.')

def deletarCliente(lista):
    vetor = []

    if len(lista) == 0:
        print('Sem clientes cadastrados.')
        return
    listarClientes(lista)

    while True:
        indice = input('Digite o número do cliente que deseja excluir: ')
        if indice.isdigit():
            indice = int(indice)
            indice -= 1

            if 0 <= indice < len(lista):
                clienteSelecionado = lista[indice]
                
                separador()
                while True:
                    print(f'Nome: {clienteSelecionado.NomeCliente}')
                    telefone = clienteSelecionado.TelefoneCliente
                    ddd = telefone[:2]
                    parte1 = telefone[2:7]
                    parte2 = telefone[7:]
                    print(f'Telefone: ({ddd}) {parte1}-{parte2}')
                    print(f'\n{25*'=-'}\n')
                    
                    print('###--Comfirme--###')
                    print('Deseja mesmo excluir esse cliente?')
                    print('1- SIM\n2- NÃO\n0- Voltar')
                    opcao = input('Digite a opção: ')
                    if opcao == '1':
                        lista.pop(indice)
                        salvarClientes(lista)
                        vetor.append(clienteSelecionado)
                        print(f'Cliente {clienteSelecionado.NomeCliente} excluido com sucesso.')
                        return
                        
                    elif opcao == '2':
                        break
                        
                    elif opcao == '0':
                        print('Voltando.')
                        return

                    else:
                        print('Opção inválida. Digite uma opção válida.')



        elif indice.strip() == '':
            print('Este campo não pode ficar vazio.')    
            print(50*'-')
        
        else:
            print('Digite apenas números.')
            print(50*'-')