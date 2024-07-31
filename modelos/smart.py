class Smart():

    NAO_INICIADA = 1
    INICIADA = 2
    CONCLUIDA = 3

    STATUS = {
        NAO_INICIADA: 'Não Iniciada',
        INICIADA: 'Iniciada',
        CONCLUIDA: 'Concluída',
    }

    def __init__(self, especifica="", mensuravel="", atingivel="", relevante="", temporizavel="", status=NAO_INICIADA):
        self._especifica = especifica
        self._mensuravel = mensuravel
        self._atingivel = atingivel
        self._relevante = relevante
        self._temporizavel = temporizavel
        self._status = status

    def __str__(self):
        return self._status