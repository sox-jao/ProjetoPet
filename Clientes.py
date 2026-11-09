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
        numero = input('Telefone do Cliente: ').strip()
        if numero.isdigit():
            registro.TelefoneCliente = numero
            break 
    return registro
    
def listarClientes(lista):
    if len(lista) == 0:
        print('Sem clientes cadastrados!')
    else:
        for x in lista: 
            print(f'Nome: {x.NomeCliente}')
            print(f'Telefone: {x.TelefoneCliente}')
            print(20*'-')

def contarClientes(lista):
    print(len(lista))