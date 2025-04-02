import unittest

from banco.transacao.Deposito import Deposito

class TestDeposito(unittest.TestCase):
    """Classe de testes para a classe Depósito."""

    def setUp(self):
        """Configuração dos objetos PessoaFísica, ContaCorrente e Depósito."""
        self.deposito = Deposito(100.00, "Depósito")
        
    def test_transacao_valor_deposito(self):
        """Teste para validar a transação valor do Depósito."""
        self.assertEqual(self.deposito.get_valor(), 100.00)        

    def test_transacao_tipo_deposito(self):
        """Teste para validar a transação tipo do Depósito."""
        self.assertEqual(self.deposito.get_tipo(), "Depósito")      