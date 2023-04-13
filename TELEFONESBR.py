import re


class TelefonesBr:
    def __init__(self, telefone):
        if self.valida(telefone):
            self.numero = telefone
        else:
            raise ValueError('Telefone incorreto')

    def __str__(self):
        return f'Telefone: {self.format()}'

    def valida(self, telefone):
        padrao = '([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
        resposta = re.findall(padrao, telefone)
        if resposta:
            return True
        else:
            return False

    def format(self):
        padrao = '([0-9]{2,3})?([0-9]{2})([0-9]{5})([0-9]{4})'
        resposta = re.search(padrao, self.numero)
        num_format = f'+{resposta.group(1)} ({resposta.group(2)}) {resposta.group(3)}-{resposta.group(4)}'
        return num_format