from arquivos import *


listatrans = abrearquivo('listatrans')
dftrans = pd.DataFrame(listatrans)
gravaarquivoqdf('dftrans', dftrans)

listameios = abrearquivo('listameios')
dfmeios = pd.DataFrame(listameios)
dfmeios = dfmeios.set_index('cod')
gravaarquivoqdf('dfmeios', dfmeios)

listacontas = abrearquivo('listacontas')
dfcontas = pd.DataFrame(listacontas)
gravaarquivoqdf('dfcontas', dfcontas)

listacontasprevisto = abrearquivo('listacontasprevisto')
dfcontasprevisto = pd.DataFrame(listacontasprevisto)
gravaarquivoqdf('dfcontasprevisto', dfcontasprevisto)

listainvest = abrearquivo('listainvest')
dfinvest = pd.DataFrame(listainvest)
gravaarquivoqdf('dfinvest', dfinvest)

basemesano = abrearquivo('basemesano')
dfmesano = pd.DataFrame(basemesano)
gravaarquivoqdf('dfmesano', dfmesano)

listaemprest = abrearquivo('listaemprest')
dfemprest = pd.DataFrame(listaemprest)
gravaarquivoqdf('dfemprest', dfemprest)
