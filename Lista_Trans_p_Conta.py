from arquivos import *
# import numpy as np
from datetime import date

dftrans = abrearquivodf('dftrans')
dfcontas = abrearquivodf('dfcontas')
dfcontas = dfcontas.rename(columns={'nome': 'conta'})
dfcontasprevisto = abrearquivodf('dfcontasprevisto')
dfcontasprevisto = dfcontasprevisto.rename(columns={'nome': 'conta'})

ano = date.today().year
mes = date.today().month

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
# print(dftrans.columns)

conta = input('Conta: ')
a = dftrans[(dftrans['conta'] == conta) & (dftrans['mes'] == mes) & (dftrans['ano'] == ano)]
print(a)
print(f'Total da Conta {conta} é {a["valor"].sum():10,.2f}')
# a = dftrans.pivot_table(values='valor', index='conta', columns='mes',
#                          aggfunc=[np.sum], margins=True)
