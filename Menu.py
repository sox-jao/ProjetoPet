from Clientes import *
def separador():
    print(50*'-')

clientes = []
while True:
    print('####----SISTEMA PETSHOP----####')
    print('1- Gerenciar clientes.\n2- Gerenciar animais.\n3- Gerenciar produtos.\n0- Sair.')
    print(50* '-=')
    
    OpcaoMenuPrincipal = input('Digite a opção: ').strip()
    
    if OpcaoMenuPrincipal == '1':
        while True:
            print('####----Gerenciar Clientes----####')
            print('1- Cadastrar novo cliente.\n2- Lista clientes.\n3- Quantidade de clientes cadastrados.\n0- Voltar ao menu inicial.')
            print(50* '-=')
            OpcaoMenuCliente = input('Digite a opção: ')
            
            if OpcaoMenuCliente == '1':
                cliente = registrarCliente()
                clientes.append(cliente)
                print('Cliente registrado com sucesso!')
                separador()
            
            elif OpcaoMenuCliente == '2':
                listarClientes(clientes)
                separador()

            elif OpcaoMenuCliente == '3':
                contarClientes(clientes)
                separador()
            
            elif OpcaoMenuCliente == '0': 
                print('Voltando!')
                separador()
                break
            
            else:
                print('Opcão inválida!')
                separador()
                
    elif OpcaoMenuPrincipal == '2': 
        while True:
            print('####----Gerenciar Clientes----####')
            print('1- Cadastrar novo Animal.\n2- Lista de Animais.\n3- Quantidade de Animais cadastrados.\n0- Voltar ao menu inicial.')
            print(50* '-=')
            OpcaoMenuAnimal = input('Digite a opção: ')


    elif OpcaoMenuPrincipal == '3':
        print('Área em desenvolvimento!')
    elif OpcaoMenuPrincipal == '0':
        print('Encerrando progama!')
        break
    else:
        print('Opção inválida!')
