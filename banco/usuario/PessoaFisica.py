from banco.usuario.Usuario import Usuario

class PessoaFisica(Usuario):
    """ Classe que representa Pessoa Física
        e estende Usuário. 

    Atributos:
        nome (str): O usuário do sistema.
        cpf (str): O cpf do usuário.
        tipo_usuario (str): O tipo de usuário 
    """
    def __init__(self, nome, cpf):
        super().__init__(nome)
        self.cpf = cpf
        self.tipo_usuario = "Pessoa Física"

    def get_cpf(self):
        """Acessa o cpf do usuário.

        Retorna:
            str: O cpf do usuário.
        """
        return self.cpf      

    def get_tipo_usuario(self):
        """Acessa o tipo de usuário.

        Retorna:
            str: O tipo do usuário.
        """
        return self.tipo_usuario

    def __str__(self):
        """Acessa uma representação dos atributos de pessoa física.

        Retorna:
            nome (str): O nome do usuário.
            cpf (str): O cpf do usuário.
            tipo_usuario (str): O tipo de usuário.
        """
        return f"{self.nome} || {self.cpf} || {self.tipo_usuario}"