from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome
    
    @abstractmethod
    def get_tipo_usuario(self):
        pass

    def __str__(self):
        """Acessa uma representação dos atributos do usuário.

        Retorna:
            nome (str): O nome do usuário.
        """
        return f"{self.nome}"