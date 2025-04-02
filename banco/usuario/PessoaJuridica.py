from banco.usuario.Usuario import Usuario

class PessoaJuridica(Usuario):
    """ Classe que representa Pessoa Jurídica. 
        e estende Usuário. 

    Atributos:
        nome (str): O usuário do sistema.
        cpf (str): O cpf do usuário.
        tipo_usuario (str): O tipo de usuário 
    """
    def __init__(self, nome, cnpj):
        super().__init__(nome)
        self.cnpj = cnpj
        self.tipo_usuario = "Pessoa Jurídica"

    def get_cnpj(self):
        """Acessa o cnpj do usuário.

        Retorna:
            str: O cpf do usuário.
        """
        return self.cnpj      

    def get_tipo_usuario(self):
        """Acessa o tipo de usuário.

        Retorna:
            str: O tipo do usuário.
        """
        return self.tipo_usuario
