import unittest

from banco.transacao.Saque import Saque

class TestSaque(unittest.TestCase):
    """Classe de testes para a classe Saque."""

    def setUp(self):
        """Configuração dos objetos PessoaFísica, ContaCorrente e Depósito."""
        self.saque = Saque(100.00, "Saque")
        
    def test_transacao_valor_saque(self):
        """Teste para validar a transação valor do Saque."""
        self.assertEqual(self.saque.get_valor(), 100.00)        

    def test_transacao_tipo_saque(self):
        """Teste para validar a transação tipo do Saque."""
        self.assertEqual(self.saque.get_tipo(), "Saque")   