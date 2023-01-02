#Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética. 
#d) Em que posição está o time da Chapecoense.

times = ('Palmeiras', 'Internacional', 'Flamengo', 'Fluminense', 'Corinthias', 'Atletico-PR', 'Atletico-MG', 'Fortaleza', 'São Paulo', 'Botafogo', 'America-MG', 'Santos', 'Goias', 'Bragantino', 'Coritiba', 'Atletico Goianiense', 'Ceará', 'Cuiabá', 'Avaí', 'Juventude')
print('Os 5 primeiros times do brasileirão são: {}!'.format(times[0:5]))
print('Os 5 ultimos times do brasileirão são: {}!'.format(times[-1:-6:-1]))
print('Os times separados em ordem alfabetica são:\n{}'.format(sorted(times)))
print('A posição do time do Atletico PR é {}ª lugar!'.format(times.index('Atletico-PR')+1))
