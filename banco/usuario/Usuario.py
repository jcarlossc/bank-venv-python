from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome
    
    @abstractmethod
    def get_tipo_usuario(self):
        pass