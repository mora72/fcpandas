from arquivos import *
import numpy as np
from datetime import date

dftrans = abrearquivodf('dftrans')
dfcontas = abrearquivodf('dfcontas')
dfcontas = dfcontas.rename(columns={'nome': 'conta'})
dfcontasprevisto = abrearquivodf('dfcontasprevisto')
dfcontasprevisto = dfcontasprevisto.rename(columns={'nome': 'conta'})

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

print(dftrans.columns)
print(dfcontas.columns)
df = pd.merge(dftrans, dfcontas, how="left", left_on='conta', right_on='conta')
a = df[df['tipo']=="D"].pivot_table(values='valor', index='conta', columns='mes',
                          aggfunc=[np.sum], margins=True)
print(a)
