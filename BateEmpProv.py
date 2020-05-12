from arquivos import *

dfemprest = abrearquivodf('dfemprest')
dftrans = abrearquivodf('dftrans')
# dfmesano = abrearquivodf('dfmesano')

# ano = dfmesano.iloc[0].ano
# mes = dfmesano.iloc[0].mes

# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', None)
# print(dfemprest.columns)
# Index(['nome', 'saldoini', 'mes', 'ano', 'realizado', 'saldofim'], dtype='object')

# e = dfemprest[(dfemprest['mes'] == 5) & (dfemprest['ano'] == 2020)]
# print(e)

# print(dftrans.columns)
# Index(['ano', 'mes', 'dia', 'valor', 'conta', 'descr', 'meio', 'nomeemprest'], dtype='object')
t_e = dftrans[(dftrans['mes'] == 5) & (dfemprest['ano'] == 2020)]
