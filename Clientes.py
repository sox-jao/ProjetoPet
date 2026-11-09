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
        for x in lista:
            Y = x.TelefoneCliente 
            ddd = Y[:2]
            parte1 = Y[2:7]
            parte2 = Y[7:] 
            print(f'Nome: {x.NomeCliente}')
            print(f'Telefone: ({ddd}) {parte1}-{parte2}')
            print(20*'-')
        
def contarClientes(lista):
    print(len(lista))