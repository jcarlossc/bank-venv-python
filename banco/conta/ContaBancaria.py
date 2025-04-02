from abc import ABC, abstractmethod
from banco.historico.Historico import Historico

class ContaBancaria(ABC):
    """Classe que representa a ContaBancária. 

    Atributos:
        usuário (Usuario): O instância Usuário.
    """
    def __init__(self, usuario):
        self.usuario = usuario
        self.saldo = 0.0
        self.historico = Historico()

    def get_usuario(self):
        """Acessa a instância Usuário.

        Retorna:
            float: O Usuário.
        """
        return self.usuario    

    def get_saldo(self):
        """Acessa o saldo da conta.

        Retorna:
            float: O saldo.
        """
        return self.saldo

    def get_historico(self):
        """Acessa o histórico.

        Retorna:
            histórico: O Histórico.
        """
        return self.historico    

    @abstractmethod
    def get_tipo_conta(self):
        """Acessa o tipo de conta.
           Método abstrato. 

        Retorna:
            str: O tipo de conta.
        """
        pass    

    @abstractmethod
    def depositar(self, valor):
        """Deposita valor na conta.
           Método abstrato .

        Retorna:
            None.
        """
        pass

    @abstractmethod
    def sacar(self, valor):
        """Saca valor da conta.
           Método abstrato .

        Retorna:
            None.
        """
        pass   

    def __str__(self):
        """Acessa uma representação dos atributos do Depósito.

        Retorna:
            usuário (Usuário): O usuário da conta.
            saldo (float): O saldo da conta.
        """
        return f"{self.usuario} {self.saldo}"  