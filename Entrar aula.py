import webbrowser
import datetime
import time

# Solicita ao usuário as informações necessárias para abrir a página no navegador
link = input("Digite o link da página: ")
dia_semana = input("Digite o dia da semana (ex: segunda, terca, quarta, quinta, sexta, sabado, domingo): ")
horario = input("Digite o horário no formato HH:MM (ex: 10:30): ")

# Converte o dia da semana e horário para um objeto datetime
hoje = datetime.date.today()
dia = hoje.weekday()
dias_semana = ['segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo']
dia_escolhido = dias_semana.index(dia_semana.lower())
diferenca_dias = (dia_escolhido - dia) % 7
data_agendada = hoje + datetime.timedelta(days=diferenca_dias)
horario_agendado = datetime.datetime.strptime(horario, '%H:%M').time()

# Calcula o tempo restante até a data e hora agendadas
agendamento = datetime.datetime.combine(data_agendada, horario_agendado)
agora = datetime.datetime.now()
tempo_restante = (agendamento - agora).total_seconds()

# Aguarda o tempo restante até a data e hora agendadas
if tempo_restante > 0:
    time.sleep(tempo_restante)

# Abre a página no navegador
webbrowser.open(link)
