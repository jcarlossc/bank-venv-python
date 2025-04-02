import unittest

from banco.usuario.PessoaJuridica import PessoaJuridica

class TestPessoaJuridica(unittest.TestCase):
    """Classe de testes para a classe PessoaFísica."""

    def setUp(self):
        """Configuração do objeto PessoaFísica."""
        self.pessoa_juridica = PessoaJuridica("soares", "12345678978989")

    def test_busca_nome(self):
        """Teste que deve retornar o nome de PessoaJurídica."""
        self.assertEqual(self.pessoa_juridica.get_nome(), "soares")     

    def test_busca_cnpj(self):
        """Teste que deve retornar o cnpj de PessoaJurídica."""
        self.assertEqual(self.pessoa_juridica.get_cnpj(), "12345678978989")  