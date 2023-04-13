from ACESSOCEP import BuscaEndereco
from CPFCNPJ import Documento
from TELEFONESBR import TelefonesBr

# Os dados dos documentos são fictícios
telefone = '55511999999999'
cpf = '36589551049'
cnpj = '18597713000140'
cep = '01001000'

# Acessando as classes
obj_telefone = TelefonesBr(telefone)
obj_cpf = Documento.cria_documento(cpf)
obj_cnpj = Documento.cria_documento(cnpj)
obj_cep = BuscaEndereco(cep)

# Saída
print(obj_telefone)
print(obj_cpf)
print(obj_cnpj)
print(obj_cep)
