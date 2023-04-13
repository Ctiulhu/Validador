from datetime import datetime

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.momento_cadastro.strftime('%d/%m/%Y - %H:%M')

    def mes_cadastro(self):
        meses_ano = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
        mes_cadastro = self.momento_cadastro.month -1
        return meses_ano[mes_cadastro]

    def dia_semana(self):
        dias_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
        dia_semana = self.momento_cadastro.weekday()
        return dias_semana[dia_semana]

    def tempo_cadastro(self):
        tempo_cadastro = datetime.today() - self.momento_cadastro
        return tempo_cadastro
