from datetime import datetime, timedelta

day = '12/Oct/2013'
dt = datetime.strptime(day, '%d/%b/%Y')
start = dt - timedelta(days=dt.weekday())
end = start + timedelta(days=6)
print(start)
print(end)

# A ideia é que quando a API estiver completamente funcional, inserido a data da semana, sejam realizadas as requisições que se encontram nas respectivas datas que se enquadram na semana.