import unittest

from banco.usuario.PessoaFisica import PessoaFisica

class TestPessoaFisica(unittest.TestCase):
    """Classe de testes para a classe PessoaFísica."""

    def setUp(self):
        """Configuração do objeto PessoaFísica."""
        self.pessoa_fisica = PessoaFisica("carlos", "12345678989")

    def test_busca_nome(self):
        """Teste que deve retornar o nome de PessoaFísica."""
        self.assertEqual(self.pessoa_fisica.get_nome(), "carlos")     

    def test_busca_cpf(self):
        """Teste que deve retornar o cpf de PessoaFísica."""
        self.assertEqual(self.pessoa_fisica.get_cpf(), "12345678989")     