from arquivos import *


# listatrans = abrearquivo('listatrans')
# dftrans = pd.DataFrame(listatrans)
# dftrans.style.to_excel('trans.xlsx', engine='openpyxl')

# listameios = abrearquivo('listameios')
# dfmeios = pd.DataFrame(listameios)
# dfmeios.style.to_excel('meios.xlsx', engine='openpyxl')

# listacontas = abrearquivo('listacontas')
# dfcontas = pd.DataFrame(listacontas)
# dfcontas.style.to_excel('contas.xlsx', engine='openpyxl')

# listacontasprevisto = abrearquivo('listacontasprevisto')
# dfcontasprevisto = pd.DataFrame(listacontasprevisto)
# dfcontasprevisto.style.to_excel('contasprevisto.xlsx', engine='openpyxl')

listameiossaldo = abrearquivo('listameiossaldo')
dfmeiossaldo = pd.DataFrame(listameiossaldo)
dfmeiossaldo.style.to_excel('meiossaldo.xlsx', engine='openpyxl')

listacontaprovisaosaldo = abrearquivo('listacontaprovisaosaldo')
dfcontaprovisaosaldo = pd.DataFrame(listacontaprovisaosaldo)
dfcontaprovisaosaldo.style.to_excel('contaprovisaosaldo.xlsx', engine='openpyxl')

listainvest = abrearquivo('listainvest')
dfinvest = pd.DataFrame(listainvest)
dfinvest.style.to_excel('invest.xlsx', engine='openpyxl')

listaemprest = abrearquivo('listaemprest')
dfemprest = pd.DataFrame(listaemprest)
dfemprest.style.to_excel('emprest.xlsx', engine='openpyxl')

basemesano = abrearquivo('basemesano')
dfmesano = pd.DataFrame(basemesano)
dfmesano.style.to_excel('mesano.xlsx', engine='openpyxl')
