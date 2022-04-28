from controller.controller import * 

def view():  
    lista_paises = get_linked_list() 

    while True:
        try:
            menu = input()
            menu = menu.split()  

            menu[0] = menu[0].upper() if menu != [] else menu.append('') 
            l = len(menu)  
    
            if menu[0] == 'RPI' and l == 2:
                command_rpi(menu[1], lista_paises)
            elif menu[0] == 'RPF' and l == 2:  
                command_rpf(menu[1], lista_paises)  
            elif menu[0] == 'RPDE' and l == 3: 
                command_rpde(menu[1:], lista_paises)
            elif menu[0] == 'RPAE' and l == 3: 
                command_rpae(menu[1:], lista_paises)
            elif menu[0] == 'RPII' and l == 3: 
                command_rpii(menu[1:], lista_paises)
            elif menu[0] == 'VNE' and l == 1: 
                command_vne(lista_paises)
            elif menu[0] == 'VP' and l == 2: 
                command_vp(menu[1], lista_paises)
            elif menu[0] == 'EPE' and l == 1: 
                command_epe(lista_paises)
            elif menu[0] == 'EUE' and l == 1: 
                command_eue(lista_paises)
            elif menu[0] == 'EP' and l == 2: 
                command_ep(menu[1], lista_paises)
            else:
                print("Por favor verifique se todas as informações foram introduzidas.") if menu != [None] else ''

        except EOFError as error:
            #print(f'error: {error}')
            break

def command_rpi(args:str, lista_paises:object) -> None: 
    controller_rpi(args, lista_paises)
    print_list(lista_paises)

def command_rpf(args:str, lista_paises:object) -> None: 
    controller_rpf(args, lista_paises)
    print_list(lista_paises)

def command_rpae(args:list[str], lista_paises:object) -> None: 
    controller_rpae(tuple(reversed(args)), lista_paises)
    print_list(lista_paises)

def command_rpde(args:list[str], lista_paises:object) -> None: 
    controller_rpde(tuple(reversed(args)), lista_paises)
    print_list(lista_paises)

def command_rpii(args:list[str], lista_paises:object) -> None: 
    args[1] = int(args[1])
    controller_rpii(tuple(reversed(args)), lista_paises)
    print_list(lista_paises)

def command_vne(lista_paises:object) -> None: 
    print(f"O número de elementos são {controller_vne(lista_paises)}.") 

def command_vp(args:str, lista_paises:object) -> None: 
    if controller_vp(args, lista_paises): 
        print(f"O país {args} encontra-se na lista.")
    else: 
        print(f"O país {args} não se encontra na lista.")  

def command_epe(lista_paises:object) -> None:  
    print(f"O país {controller_epe(lista_paises)} foi eliminado da lista.")

def command_eue(lista_paises:object) -> None:  
    print(f"O país {controller_eue(lista_paises)} foi eliminado da lista.")

def command_ep(args:str, lista_paises:object) -> None: 
    if controller_vp(args, lista_paises): 
        controller_ep(args, lista_paises)
        print(f"O país {args} foi eliminado da lista.")
    else: 
        print(f"O país {args} não se encontra na lista.")  
    
