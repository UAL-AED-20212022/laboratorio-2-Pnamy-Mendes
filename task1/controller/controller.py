from models.LinkedList import LinkedList

def get_linked_list(): 
    return LinkedList()

def print_list(lista_paises: object):
    lista_paises.traverse_list()

def controller_rpi(args:str, lista_paises: object):
    lista_paises.insert_at_start(args)

def controller_rpf(args:str, lista_paises: object):
    lista_paises.insert_at_end(args)

def controller_rpae(args:tuple, lista_paises: object):
    lista_paises.insert_before_item(*args)

def controller_rpde(args:tuple, lista_paises: object):
    lista_paises.insert_after_item(*args)

def controller_rpii(args:tuple, lista_paises: object):
    lista_paises.insert_at_index(*args)

def controller_vne(lista_paises: object) -> int:
    return lista_paises.get_count()

def controller_vp(args:str, lista_paises: object):
    return lista_paises.search_item(args)

def controller_epe(lista_paises: object):
    pais = lista_paises.start_node.item
    lista_paises.delete_at_start()
    return pais

def controller_eue(lista_paises: object):
    pais = lista_paises.get_last_node()
    lista_paises.delete_at_end()
    return pais

def controller_ep(args: str, lista_paises: object):
    lista_paises.delete_element_by_value(args)