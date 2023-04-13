from validate_docbr import CPF, CNPJ
from DATAS import DatasBr


class Documento:
    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError('Quantidade de digitos incorreta!!')


class DocCpf:

    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
            self.data = DatasBr()
        else:
            raise ValueError('CPF inválido')

    def __str__(self):
        return f'Cpf: {self.format()}, data de registro: {self.data}'

    def valida(self, documento):
            validador_cpf = CPF()
            return validador_cpf.validate(documento)

    def format(self):
        mascara_cpf = CPF()
        return mascara_cpf.mask(self.cpf)


class DocCnpj:

    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
            self.data = DatasBr()
        else:
            raise ValueError('Cnpj inválida')

    def __str__(self):
        return f'Cnpj: {self.format()}, data de registro: {self.data}'

    def valida(self, documento):
        validador_cnpj = CNPJ()
        return validador_cnpj.validate(documento)

    def format(self):
        mascara_cnpj = CNPJ()
        return mascara_cnpj.mask(self.cnpj)