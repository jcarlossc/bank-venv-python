from banco.transacao.Transacao import Transacao
import datetime 

class Historico:
    """Classe que representa o histórico das contas. 

    Atributos:
        None.
    """
    def __init__(self):
        self.transacoes = []
        self.data_hora = datetime.datetime.now()

    def add_transacao(self, transacao):   
        """Adiciona às transações ao histórico.

        Retorna:
            None.
        """
        transacao_dict = {
            "Valor R$": transacao.valor,
            "Tipo de Transação" : transacao.tipo,
            "Data" : self.data_hora.strftime("%d/%m/%Y"),
            "Hora" : self.data_hora.strftime("%H:%M:%S")
        }
        self.transacoes.append(transacao_dict) 

    def get_transacoes(self):
        """Acessa às transações.

        Retorna:
            array: Os transações do sistema.
        """
        return self.transacoes  

    def __str__(self):
        """Acessa uma representação das transações.

        Retorna:
            transações (array): As transações.
        """
        return f"{self.transacoes}"        