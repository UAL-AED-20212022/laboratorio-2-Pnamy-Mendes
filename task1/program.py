from view.view import view
from sys import stdout
stdout.reconfigure(encoding="utf-8")

"""
    Este programa é um Sistema de armazenamento de nomes de países, com o formato -> Linked List
    As suas funcionalidades são:

        Países:
            -> Registar País no inicio da lista. ['RPI' + nome_país_novo] (exemplo: <RPI Portugal>) 
                -> Sucesso: É apresentada a lista de países atual depois de inserido o novo país.
                
            -> Registar País no fim da lista. ['RPF' + nome_país_novo] (exemplo: <RPI Brasil>) 
                -> Sucesso: É apresentada a lista de países atual depois de inserido o novo país.

            -> Registar País Depois de outro Elemento já Registado. ['RPDE' + nome_país_novo + nome_país_registado] (exemplo: <RPI Chile Portugal>) 
                -> Sucesso: É apresentada a lista de países atual depois de inserido o novo país.

            -> Registar País Antes de outro Elemento já Registado. ['RPAE' + nome_país_novo + nome_país_registado] (exemplo: <RPI Franca Portugal>) 
                -> Sucesso: É apresentada a lista de países atual depois de inserido o novo país.

            -> Registar País num determinado Índice. ['RPII' + nome_país_novo + indice] (exemplo: <RPI Italia 1>) 
                -> Sucesso: É apresentada a lista de países atual depois de inserido o novo país.

            -> Verificar Número de elementos da lista. ['VNE'] (exemplo: <VNE>) 
                -> Sucesso: O número de elementos são <número_elementos>.

            -> Verificar se um País se encontra na lista. ['VP' + nome_pais] (exemplo: <VP Portugal>) 
                -> Sucesso: O país <nome_país> encontra-se na lista.
                -> Insucesso: O país <nome_país> não se encontra na lista.

            -> Eliminar o primeiro elemento da lista. ['EPE'] (exemplo: <EPE>) 
                -> Sucesso: O país <nome_país_eliminado> foi eliminado da lista.

            -> Eliminar o último elemento da lista. ['EUE'] (exemplo: <EUE>) 
                -> Sucesso: O país <nome_país_eliminado> foi eliminado da lista.

            -> Eliminar um determinado país da lista. ['EP' + nome_país] (exemplo: <EP Portugal>) 
                -> Sucesso: O país <nome_país_eliminado> foi eliminado da lista.
                -> Insucesso: O país <nome_país> não se encontra na lista.

            
    Os requerimento do programa são:
        Nenhum.

    
    Nenhum módulo extra é usado, sendo unicamente necessário o Python v3.10 para executar o prgrama.
"""

def main() -> None:
    """ Chama a função do view para executar. """
    view()


if __name__ == '__main__':
    main()
