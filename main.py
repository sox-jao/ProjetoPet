import Clientes
def separador():
    print(50*'-')

clientes = Clientes.carregarClientes()
while True:
    print('####----SISTEMA PETSHOP----####')
    print('1- Gerenciar clientes.' \
    '\n2- Gerenciar animais.' \
    '\n3- Gerenciar produtos.' \
    '\n0- Sair.')
    print(50* '-=')
    
    OpcaoMenuPrincipal = input('Digite a opção: ').strip()
    
    if OpcaoMenuPrincipal == '1':
        while True:
            print('####----Gerenciar Clientes----####')
            print('1- Cadastrar novo cliente.' \
            '\n2- Lista clientes.' \
            '\n3- Quantidade de clientes cadastrados.' \
            '\n4- Atualizar Cliente.'
            '\n0- Voltar ao menu inicial.')
            print(50* '-=')
            OpcaoMenuCliente = input('Digite a opção: ')
            
            if OpcaoMenuCliente == '1':
                cliente = Clientes.registrarCliente()
                clientes.append(cliente)
                Clientes.salvarClientes(clientes)
                print('Cliente registrado com sucesso!')
                separador()
            
            elif OpcaoMenuCliente == '2':
                Clientes.listarClientes(clientes)
                separador()

            elif OpcaoMenuCliente == '3':
                Clientes.contarClientes(clientes)
                separador()
            
            elif OpcaoMenuCliente == '0': 
                print('Voltando!')
                separador()
                break
            
            else:
                print('Opcão inválida!')
                separador()
                
    elif OpcaoMenuPrincipal == '2': 
        print('Área em desenvolvimento!')
    elif OpcaoMenuPrincipal == '3':
        print('Área em desenvolvimento!')
    elif OpcaoMenuPrincipal == '0':
        print('Encerrando progama!')
        break
    else:
        print('Opção inválida!')
