import requests


class BuscaEndereco:
    def __init__(self, documento):
        documento = str(documento)
        if self.cep_valido(documento):
            self.cep = documento
        else:
            raise ValueError('Documento inválido!')

    def __str__(self):
        return f'Cep: {self.format()}: {self.acessa()}'

    def cep_valido(self, documento):
        if len(documento) == 8:
            return True
        else:
            return False

    def format(self):
        return f'{self.cep[0:5]}-{self.cep[5:]}'

    def acessa(self):
        url = f'https://viacep.com.br/ws/{self.cep}/json/'
        acesso = requests.get(url)
        dados = acesso.json()
        return(dados['bairro'], dados['localidade'], dados['uf'])