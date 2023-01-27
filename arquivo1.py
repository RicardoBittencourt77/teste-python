from datetime import date

sem = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")

dia_da_semana = date.today().weekday()

if dia_da_semana < 5:
    diaSemana = (f"{sem[dia_da_semana]}-feira")
else:
    diaSemana = (f"{sem[dia_da_semana]}")

print('Olá mundo! Hoje é {}!'.format(diaSemana))