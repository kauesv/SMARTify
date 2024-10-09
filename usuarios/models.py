from datetime import datetime

class Usuarios:
    def __init__(self, nome: str, sobrenome: str, criado_em, atualizado_em, deletado: bool):
        self.nome = nome
        self.sobrenome = sobrenome
        self.criado_em = criado_em if criado_em else datetime.now()
        self.atualizado_em = atualizado_em if atualizado_em else datetime.now()
        self.deletado = deletado