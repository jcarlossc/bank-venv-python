class Extrato:
    """Classe que representa o extrato das contas. 

    Atributos:
        None.
    """
    def __init__(self):
        pass
        
    def get_extrato(conta):
        """Imprime extrato.

        Retorna:
            None.
        """
        print("---------------------------------------- EXTRATO ----------------------------------------")
        print(f"TIPO DE CONTA: {conta.get_tipo_conta()}")
        print(f"TITULAR: {conta.get_usuario().get_nome()}")
        print(f"CPF: {conta.get_usuario().get_cpf()}")
        print(f"SALDO: R$ {round(conta.get_saldo(), 2)}")
        print("LISTA DE TRANSAÇÕES")
        for transacao in conta.get_historico().get_transacoes():
            print(transacao)
        print("------------------------------------------ FIM ------------------------------------------")