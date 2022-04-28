from view.view import view
from sys import stdout
stdout.reconfigure(encoding="utf-8")

"""
    Este programa serve para a gestão de consultores e a gestão dos seus imóveis para venda.
    As suas funcionalidades são:

        Consultores:
            -> Registar Consultor. ['RC' + nome + apelido + NIF] (exemplo: <RC Maria Santos 123123333>) 
                -> Sucesso: 'Consultor registado com sucesso.'
                -> Insucesso: 
                    -> Consultor já registado (verificação por NIF): 'Não é possível realizar o registo,consultor já registado.'
                    -> Campos Insuficientes: 'Por favor verifique se todas as informações foram introduzidas.'

            -> Eliminar Consultor. ['EC' + NIF] (exemplo: <EC 123123333> ) 
                -> Sucesso: 
                    'Consultor eliminado com sucesso.' 
                    'Os imóveis <lista_ID_imoveis> também foram eliminados
                        <lista_ID_imoveis> -> String de todos os Ids dos imoveis que pertenciam ao Consultor eliminado.
                -> Insucesso: 
                    -> NIF inválido: 'Não é possível realizar a operação,NIF inválido.'
                    -> Campos Insuficientes: 'Por favor verifique se todas as informações foram introduzidas.'

            Imóveis:
                -> Registar Imóvel. ['RI' + NIF_consultor + localizacao_imovel + area_util + tipologia_imovel + ano_imovel + valor_venda_imovel + comissao_venda_imovel] 
                    (exemplo: <RI 123123333 Porto 170 T4 2020 400000€ 0.20>)  
                    -> Sucesso: 'Imóvel com <ID> registado com sucesso.' 
                        <ID> -> Integer único gerado pelo programa.
                    -> Insucesso: 
                        -> NIF inválido: 'Não é possível realizar o registo do imóvel,NIF inválido.'
                        -> Campos Insuficientes: 'Por favor verifique se todas as informações foram introduzidas.'

                -> Listar imóveis dum consultor. ['LI' + NIF] (exemplo: <LI 123123333>)
                    -> Sucesso: 
                        -> Com imóveis registados: '<ID_imovel> <valor_venda_imovel> <comissao_venda_imovel>.' para cada imóvel pertencente ao consultor.
                            <ID_imovel> -> Integer único gerado pelo programa que repreenta o imóvel.
                            <valor_venda_imovel> -> Valor do Imóvel em euros (€).
                            <comissao_venda_imovel> -> Comissão de venda do Imóvel.
                        -> Sem imóveis registados: 'Não existem imóveis registados.'
                    -> Insucesso: 
                        -> NIF inválido: 'Não é possível realizar o registo do imóvel,NIF inválido'
                        -> Campos Insuficientes: 'Por favor verifique se todas as informações foram introduzidas.'

                -> Eliminar Imóvel. ['EI' + NIF + ID_imóvel] (exemplo: <EI 123123333 1>)
                    -> Sucesso: 'Imóvel eliminado com sucesso.'
                    -> Insucesso: 
                        -> Imóvel não registado: 'O ID indicado n«é inválido.'
                        -> Imóvel não pertence ao NIF indicado: 'O imóvel <ID_imovel> não pertence ao consultor indicado.'
                        -> Campos Insuficientes: 'Por favor verifique se todas as informações foram introduzidas.'
"""

def main() -> None:
    """ Chama a função do view para executar. """
    view()


if __name__ == '__main__':
    main()
