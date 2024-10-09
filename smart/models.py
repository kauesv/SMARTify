from datetime import datetime

class Smart:
    def __init__(self, usuario_id: str, especifica: str, mensuravel: str, atingivel: str, relevante: str, temporizavel: str, status: list, criado_em, atualizado_em, deletado: bool):
        self.usuario_id = usuario_id
        self.especifica = especifica
        self.mensuravel = mensuravel
        self.atingivel = atingivel
        self.relevante = relevante
        self.temporizavel = temporizavel
        self.status = status
        self.criado_em = criado_em if criado_em else datetime.now()
        self.atualizado_em = atualizado_em if atualizado_em else datetime.now()
        self.deletado = deletado