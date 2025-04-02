from banco.conta.ContaBancaria import ContaBancaria
from banco.transacao.Deposito import Deposito
from banco.transacao.Saque import Saque

class ContaPoupanca(ContaBancaria):
    """Classe que representa a ContaPoupança. 

    Atributos:
        usuário (Usuario): O instância Usuário.
    """
    def __init__(self, usuario):
        super().__init__(usuario)

    def depositar(self, valor):
        """Deposita valor na conta.
           Processa o depósito
           Adiciona o depósito ao histórico
        
        Retorna:
            None.
        """
        self.saldo += valor  
        self.historico.add_transacao(Deposito(valor, "Depósito"))
        return valor

    def sacar(self, valor):
        """Saca valor da conta.
           Processa o saque
           Adiciona o saque ao histórico

        Retorna:
            None.
        """
        self.saldo -= valor 
        self.historico.add_transacao(Saque(valor, "Saque"))   
        return valor

    def get_tipo_conta(self):
        """Acessa o tipo de conta.

        Retorna:
            str: O tipo de conta.
        """
        return "Conta Poupança"       

    def __str__(self):
        """Acessa uma representação dos atributos da ContaCorrente.

        Retorna:
            usuário (Usuário): O usuário da conta.
            saldo (float): O saldo da conta.
        """
        return f"{self.usuario} {self.saldo}"   